"""Proxy model for creating instances of City."""
import requests

from geo_data.models import City
from geo_data.models import Country
from geo_data.models import Variant

API_URL = 'https://geocode.xyz/'
API_KEY = '556274443501899501456x361'
API_FORMAT = 'json'
REGION = 'Europe'


class CityProxy(object):
    """City creation logic."""
    def __init__(self, city_name):
        self.city_name = city_name

    def _api_call(self):
        """API call to external service."""
        response = requests.post(API_URL, data={
            'locate': self.city_name,
            'auth': API_KEY,
            'geoit': API_FORMAT,
            'region': REGION,
        })
        return response.json()

    def create(self):
        """Creating new City instance."""
        city_info = self._api_call()
        country, _ = Country.objects.get_or_create(
            name=city_info['standard']['countryname'])
        city, _ = City.objects.get_or_create(
            name=city_info['standard']['city'],
            country=country
        )
        city.latitude = city_info['latt']
        city.longitude = city_info['longt']
        city.save()
        Variant.objects.get_or_create(name=self.city_name, city=city)
        return city

    def get(self):
        """Get or create new City instance from db."""
        try:
            variant = Variant.objects.get(name=self.city_name)
        except Variant.DoesNotExist:
            return self.create()
        else:
            return variant.city
