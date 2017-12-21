"""External api response class."""
import logging

from bus_travel.helpers import serialize

from service.base import Response
from service.base import Coordinates

logger = logging.getLogger(__name__)


class OpenCageResponse(Response):
    """OpenCage special response type."""

    @staticmethod
    def parse(data):
        """Parse input data to desired format."""
        data = data['results'][0]
        coord = Coordinates(data['geometry']['lat'], data['geometry']['lng'])
        try:
            return {
                'name': serialize(
                    data['components'].get('city') or
                    data['components'].get('county') or
                    data['components']['state']
                ),
                'country': serialize(data['components']['country']),
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
