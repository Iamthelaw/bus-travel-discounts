"""Api endpoints."""
from django.urls import path

from bus_travel.helpers import instance_view

from geo_data.serializers import FullCitySerializer
from geo_data.serializers import SimpleCitySerializer
from geo_data.serializers import SimpleCountrySerializer
from geo_data.serializers import FullCountrySerializer


# TODO Need to create some kind of unification, duplicated code
urlpatterns = [
    path(
        'city/<slug:city_name>',
        instance_view(SimpleCitySerializer)),
    path(
        'city/detail/<slug:city_name>',
        instance_view(FullCitySerializer)),
    path(
        'country/<slug:country_name>',
        instance_view(SimpleCountrySerializer)),
    path(
        'country/detail/<slug:country_name>',
        instance_view(FullCountrySerializer)),
]
