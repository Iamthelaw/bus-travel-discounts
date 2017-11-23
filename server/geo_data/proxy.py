"""Proxy model for creating instances of City."""
import logging

from geo_data.models import City
from geo_data.models import Country
from geo_data.models import Variant
from geo_data.helpers import sanitize

from service.geo import MapzenService
from service.geo import OpenCageService
from service.exceptions import ServiceNotFound, ServiceUnavailable

logger = logging.getLogger(__name__)


class CityProxy(object):
    """City creation logic."""
    def __init__(self, city_name):
        self.city_name = sanitize(city_name)
        self.opencage = OpenCageService
        self.mapzen = MapzenService

    def call_services(self):
        """Calling external api services."""
        try:
            return self.opencage.find(self.city_name)
        except (ServiceNotFound, ServiceUnavailable) as e:
            logger.exception(str(e), exc_info=0)
        try:
            return self.mapzen.find(self.city_name)
        except (ServiceNotFound, ServiceUnavailable) as e:
            logger.exception(str(e), exc_info=0)
        raise ValueError(
            'All services unable to find "%s"' % self.city_name)

    def create(self):
        """Creating new City instance."""
        city_info = self.call_services()
        country, _ = Country.objects.get_or_create(
            name=city_info['country'])
        city, _ = City.objects.get_or_create(
            name=city_info['name'],
            country=country,
        )
        city.latitude = city_info['latitude']
        city.longitude = city_info['longitude']
        city.save()
        Variant.objects.get_or_create(name=self.city_name, city=city)
        return city

    def get(self):
        """Get or create new City instance from db."""
        try:
            variant = Variant.objects.get(name=self.city_name)
        except Variant.DoesNotExist:
            logger.info(
                'Unable to find city "%s", creating...' % self.city_name)
            return self.create()
        else:
            logger.debug(
                'Found existing city "%s"' % self.city_name)
            return variant.city
