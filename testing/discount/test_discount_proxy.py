"""Tests for discount proxy class."""
import pytest

from discount.proxy import DiscountProxy

from discount.models import Discount
from discount.models import Currency

from geo_data.models import City
from geo_data.models import Country
from geo_data.models import Variant


@pytest.fixture
def city():
    """Returns City instance."""
    country = Country.objects.create(name='Latvia')
    city = City.objects.create(name='Riga', country=country)
    Variant.objects.create(name='Riga', city=city)
    return city


@pytest.fixture
def currency():
    """Returns currency instance."""
    return Currency.objects.create(code='USD', symbol='$')


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


@pytest.mark.django_db
def test_valid_kwargs(kwargs):
    """Just test that with valid input all works as expected."""
    proxy = DiscountProxy(kwargs)
    discount = proxy.get()
    assert Discount.objects.count() == 1


@pytest.mark.django_db
def test_update_process(kwargs):
    """Testing update process of proxy."""

    # Creating first instance
    evil_empire = 'http://yandex.ru'
    proxy = DiscountProxy(kwargs)
    discount = proxy.get()

    # Getting instance again
    kwargs.update(link=evil_empire, original_price=100)
    proxy = DiscountProxy(kwargs)
    discount = proxy.get()

    # No new instances created
    assert Discount.objects.count() == 1

    # Attributes are changed
    assert Discount.objects.first().link == evil_empire
    assert Discount.objects.first().original_price == 100
