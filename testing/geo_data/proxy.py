"""Tests for geo proxy class."""
import pytest
import responses
import mimesis

from django.conf import settings

from geo_data.models import City
from geo_data.proxy import CityProxy


@responses.activate
def test_call_external_api(city_name, geo_api_response):
    proxy = CityProxy(city_name, use_timeout=False)
    responses.add('GET', settings.OPENCAGE_API_URL, json=geo_api_response)
    assert proxy.call_services()


@responses.activate
@pytest.mark.django_db
def test_create_new_city_instance(city_name, geo_api_response):
    proxy = CityProxy(city_name, use_timeout=False)
    responses.add('GET', settings.OPENCAGE_API_URL, json=geo_api_response)
    assert isinstance(proxy.create(), City)


@responses.activate
@pytest.mark.django_db
def test_city_name_variant(city_name, geo_api_response):
    proxy = CityProxy(city_name, use_timeout=False)
    geo_api_response['results'][0]['components']['name'] = city_name
    responses.add('GET', settings.OPENCAGE_API_URL, json=geo_api_response)
    city = proxy.get()
    assert isinstance(city, City)
    assert city.name == city.pretty_name == city_name
