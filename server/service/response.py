"""External api response class."""
import logging

from geo_data.helpers import sanitize

from service.base import Response
from service.base import Coordinates

logger = logging.getLogger(__name__)


class MapzenResponse(Response):
    """Mapzen special response type."""

    @staticmethod
    def parse(data):
        """Parse input data to desired format."""
        data = data['features']
        coord = Coordinates(*data[0]['geometry']['coordinates'])
        return {
            'name': data[0]['properties']['name'],
            'country': data[0]['properties']['country'],
            'latitude': coord.latitude,
            'longitude': coord.longitude,
        }

    @property
    def is_empty(self):
        """This response is empty?"""
        return len(self.raw_data['features']) == 0


class OpenCageResponse(Response):
    """OpenCage special response type."""

    @staticmethod
    def parse(data):
        """Parse input data to desired format."""
        data = data['results'][0]
        coord = Coordinates(data['geometry']['lat'], data['geometry']['lng'])
        try:
            return {
                'name': sanitize(
                    data['components'].get('city')
                    or data['components'].get('county')
                    or data['components']['state']
                ),
                'country': sanitize(data['components']['country']),
                'latitude': coord.latitude,
                'longitude': coord.longitude,
            }
        except KeyError as exception:
            print(data)
            logger.debug(data)
            logger.exception(exception)

    @property
    def is_empty(self):
        """This response is empty?"""
        return self.raw_data['total_results'] == 0
