from itertools import combinations

import pytest

from discount.models import Discount


@pytest.fixture
def kwargs(city, currency):
    """Returns valid kwargs dictionary."""
    return {
        'from_city': city,
        'to_city': city,
        'original_price': 50,
        'original_currency': currency,
        'link': 'http://google.com',
        'parser': 'AnyParser'
    }


@pytest.fixture
def discount(price, page_url, city, currency):
    """Returns discount instance."""
    return Discount.objects.create(
        from_city=city,
        to_city=city,
        original_price=price,
        original_currency=currency,
        link=page_url,
    )


@pytest.fixture
def discounts(cities, price, page_url, currency):
    """Returns 10 Discount instances."""
    city_pairs = tuple(combinations(cities, 2))[:10]
    for from_city, to_city in city_pairs:
        Discount.objects.create(
            from_city=from_city,
            to_city=to_city,
            original_price=price,
            original_currency=currency,
            link=page_url
        )
