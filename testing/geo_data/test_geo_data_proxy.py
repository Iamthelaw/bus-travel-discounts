"""Tests for geo proxy class."""
from unittest import mock

import pytest

from geo_data.proxy import CityProxy

from geo_data.models import City
from geo_data.models import Country
from geo_data.models import Variant


API_ANSWER = {
    'standard': {
        'addresst': {},
        'city': 'Riga',
        'prov': 'LV',
        'countryname': 'Latvia',
        'postal': {},
        'confidence': '0.60'
    },
    'longt': '24.13265',
    'latt': '56.96143'
}


@pytest.fixture
def city():
    """Returns City instance."""
    country = Country.objects.create(name='Latvia')
    city = City.objects.create(name='Riga', country=country)
    Variant.objects.create(name='Riga', city=city)
    return city


@pytest.mark.django_db
@mock.patch.object(CityProxy, '_api_call')
def test_new_city(mocked_api_call):
    """Testing creation of new city."""
    mocked_api_call.return_value = API_ANSWER
    proxy = CityProxy('Riga')
    instance = proxy.get()

    # It calls external api only once
    assert mocked_api_call.call_count == 1

    # It creates 3 records in 3 tables in db
    assert City.objects.count() == 1
    assert Country.objects.count() == 1
    assert Variant.objects.count() == 1

    # It have name
    assert instance.name == 'Riga'


@pytest.mark.django_db
@mock.patch.object(CityProxy, '_api_call', side_effect=mock.Mock())
def test_existing_city(mocked_api_call, city):
    """Test that if city existed, it will not be created."""
    proxy = CityProxy('Riga')
    proxy.get()

    # Never creates new City instances with equal names
    assert City.objects.count() == 1

    # Never calls external api
    assert mocked_api_call.call_count == 0
