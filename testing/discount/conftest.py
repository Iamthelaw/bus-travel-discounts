import pytest

from geo_data.models import City
from geo_data.models import Country


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
