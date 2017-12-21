"""Tests management command."""
import pytest
import mimesis
import responses

from django.conf import settings

from discount.models import Discount
from parser.management.commands.parser import Command as ParserCommand
from parser.ecolines import LocalUrlParser


def city_info(count=10):
    """Returns unique cities info."""
    cities = set()
    addr = mimesis.Address()
    country = addr.country()
    while len(cities) <= 10:
        cities.add(addr.city())
    for city in cities:
        yield {
            'geometry': {
                'lat': addr.latitude(),
                'lng': addr.longitude(),
            },
            'components': {
                'name': city,
                'state': country[:2].upper(),
                'country': country,
            }
        }


@responses.activate
@pytest.mark.django_db
def test_command_can_save_offers(page_url, locales_tpl, offers_tpl, menu_tpl):

    assert Discount.objects.count() == 0
    responses.add(
        responses.GET,
        LocalUrlParser.domain,
        body=locales_tpl,
        status=200
    )
    command = ParserCommand(use_timeout=False)
    command.localized_links = [page_url]
    responses.add(
        responses.GET,
        page_url,
        body=menu_tpl,
        status=200
    )
    command.parser.url = page_url
    responses.add(
        responses.GET,
        command.parser.link_to_discounts,
        body=offers_tpl,
        status=200
    )
    for info in city_info():
        responses.add(
            responses.GET,
            settings.OPENCAGE_API_URL,
            json={
                'results': [info],
                'total_results': 1
            },
            status=200
        )
    command.handle()
    assert Discount.objects.count() <= 5
