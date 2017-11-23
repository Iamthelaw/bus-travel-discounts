"""External Geo-parsing services."""
from django.conf import settings

from service.base import Service
from service.response import OpenCageResponse
from service.response import MapzenResponse


OpenCageService = Service(settings.OPENCAGE_API, OpenCageResponse)
MapzenService = Service(settings.MAPZEN_API, MapzenResponse)
