import responses
from django.conf import settings

from geo_data.models import City
from service.base import Service
from service.response import OpenCageResponse


@responses.activate
def test_service_can_find_city_info(city_name, geo_api_response):
    geo_api_response['results'][0]['components']['city'] = city_name
    responses.add(
        'GET',
        settings.OPENCAGE_API_URL.format(query=city_name),
        json=geo_api_response, status=200)
    service = Service(
        settings.OPENCAGE_API_URL, OpenCageResponse, use_timeout=False)
    city = service.find(city_name)
    assert isinstance(city, dict)
    assert city['name'] == city_name.title()
