"""REST views for geo app."""
from bus_travel.helpers import instance_view

from geo_data.models import City, Country
from geo_data.serializers import FullCitySerializer
from geo_data.serializers import SimpleCitySerializer
from geo_data.serializers import SimpleCountrySerializer
from geo_data.serializers import FullCountrySerializer


city = instance_view(SimpleCitySerializer)
city_details = instance_view(FullCitySerializer)
country = instance_view(SimpleCountrySerializer)
country_details = instance_view(FullCountrySerializer)
