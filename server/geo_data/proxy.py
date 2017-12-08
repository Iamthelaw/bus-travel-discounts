"""
Proxy classes
=============

Main reason for city proxy class to exist is in desire to extract
interaction between data model and external api service in proxy class.
"""
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
    """
    Proxy class for city model.

    Usage

    .. code-block:: python

        proxy = CityProxy('Riga')
        city = proxy.get()

    Explanation is needed. First - we created an instance of this proxy
    class and passed a paramener ``city_name``. In our example it is ``Riga``.

    Now we can call ``get`` method of this proxy class to get city
    instance from database.

    Thae algoritm is like this:

    1. The get method tries to find matching variant of provided city name
        in database. If it succeded, it returns linked to variant model city
        model. End of method run.
    2. If get method fails to found matching variant in the database, it calls
        a proxy method ``call_services``. That method is starting to send
        requests to external api server.

        1. If external api is found information about this city, it returns to
            method ``get`` all necessary info, already formated and cleaned up
            by service class. In that case ``get`` method creatates in database
            new city record, new variant record and links them. Than returns
            city instance from database and end of ``get`` method.
        2. If external api is failed to find information about desired city,
            than we in trouble and severe letter is sended to administrator.

    """

    def __init__(self, city_name):
        self.city_name = sanitize(city_name)
        self.opencage = OpenCageService
        self.mapzen = MapzenService

    def call_services(self):
        """Calling external api services."""
        try:
            return self.opencage.find(self.city_name)
        except (ServiceNotFound, ServiceUnavailable) as exc:
            logger.exception(str(exc), exc_info=0)
        try:
            return self.mapzen.find(self.city_name)
        except (ServiceNotFound, ServiceUnavailable) as exc:
            logger.exception(str(exc), exc_info=0)
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
                'Unable to find city "%s", creating...',
                self.city_name
            )
            return self.create()
        else:
            logger.debug('Found existing city "%s"', self.city_name)
            return variant.city
