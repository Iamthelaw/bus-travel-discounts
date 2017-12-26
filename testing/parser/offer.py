import responses
import pytest
import mimesis

from django.conf import settings

from discount.models import Discount
from parser.offer import Offer


def test_can_create_offer():
    offer = Offer()
    assert offer


def test_can_parse_destinations():
    offer = Offer()
    offer.destinations = 'Riga - Oslo - Helsinki'
    assert offer.from_city == 'Riga'
    assert offer.to_city == 'Oslo'
    offer.destinations = 'Helsinki → Tromso'
    assert offer.from_city == 'Helsinki'
    assert offer.to_city == 'Tromso'
    offer.destinations = 'Algericas'
    assert offer.from_city == 'Algericas'
    assert offer.to_city is None
    offer.destinations = ''
    assert offer.from_city == ''
    assert offer.to_city is None


@pytest.mark.django_db
def test_can_parse_price():
    offer = Offer()
    offer.price_tag = '15.00 EUR'
    assert offer.price == 15.
    assert offer.currency.code == 'EUR'
    offer.price_tag = ''
    assert offer.price == 0.
    assert offer.currency.code == 'XXX'
    offer.price_tag = '10'
    assert offer.price == 10.
    assert offer.currency.code == 'XXX'


def test_can_set_link(page_url):
    offer = Offer()
    offer.link_tag = page_url
    assert offer.link == page_url


# Need to think about how to test this properly
@responses.activate
@pytest.mark.django_db
def test_can_save_offer():
    addr = mimesis.Address()
    responses.add(
        responses.GET,
        settings.OPENCAGE_API_URL,
        json={
            'results': [{
                'geometry': {
                    'lat': addr.latitude(),
                    'lng': addr.longitude(),
                },
                'components': {
                    'name': 'Riga',
                    'state': 'LV',
                    'country': 'Latvia'
                }
            }],
            'total_results': 1
        },
        status=200)
    responses.add(
        responses.GET,
        settings.OPENCAGE_API_URL,
        json={
            'results': [{
                'geometry': {
                    'lat': addr.latitude(),
                    'lng': addr.longitude(),
                },
                'components': {
                    'name': 'Helsinki',
                    'state': 'FI',
                    'country': 'finland'
                }
            }],
            'total_results': 1
        },
        status=200)
    offer = Offer(use_timeout=False)
    offer.from_city = 'Riga'
    offer.to_city = 'Helsinki'
    offer.price_tag = '15 USD'
    offer.link = ''
    offer.save()
    assert Discount.objects.count() == 1
