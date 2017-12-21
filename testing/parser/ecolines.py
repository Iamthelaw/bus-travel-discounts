"""Tests for LocalUrlParser."""
import pytest
import responses
from decimal import Decimal

from parser.offer import Offer
from money.models import Currency


@responses.activate
def test_parser_can_extract_locale_info(local_url_parser, locales_tpl):
    responses.add(
        responses.GET,
        local_url_parser.domain,
        body=locales_tpl,
        status=200
    )
    local_url_parser()
    assert local_url_parser.locales
    assert local_url_parser.collected_data
    assert all([
        url
        for url in local_url_parser.collected_data
        if url.startswith('http')
    ])


@responses.activate
@pytest.mark.django_db
def test_parser_can_collect_offers(page_url, offer_parser, menu_tpl, offers_tpl):
    responses.add(responses.GET, page_url, body=menu_tpl, status=200)
    offer_parser.url = page_url
    assert offer_parser.link_to_discounts
    assert offer_parser.link_to_discounts.startswith('http')
    responses.add(
        responses.GET,
        offer_parser.link_to_discounts,
        body=offers_tpl,
        status=200)
    offer_parser.collect()
    assert offer_parser.collected_data
    offer = tuple(offer_parser.collected_data)[0]
    assert isinstance(offer, Offer)
    assert offer.from_city
    assert offer.to_city
    assert isinstance(offer.price, Decimal)
    assert isinstance(offer.currency, Currency)
    assert offer.link.startswith('http')
