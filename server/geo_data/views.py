"""
Views
=====

This is REST views, here I created ``BaseGeoViewSet`` inherited from
:class:`rest_framework.viewsets.ViewSet`. The main reason for this is that
in this application I wanted to get short information about the geographical
object and detailed.

This ``CityViewSet`` and ``CountryViewSet`` are generating two kinds of
URLs with different serializers

* ``/<geo object>/<name>/``
* ``/<geo_object/<name>/detail/``

Detail endpoint is different because they contain information about
linked discounts. It is a lot of information but can be very handy.
"""
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from geo_data.models import City, Country
from geo_data import serializers


class BaseGeoViewSet(ViewSet):
    """
    Parent class for City and Country ViewSets.

    So there will be less duplicated code. Defines ``retrieve`` and
    ``detail`` methods that are different by serializer class.

    It is designed so when inherited from it, the child class must only
    set ``queryset``, ``retrieve_serializer`` and ``detail_serializer``
    to get all endpoints.
    """
    #: By default, this set to 'pk'
    lookup_field = 'name'

    def retrieve(self, request, name=None):
        instance = get_object_or_404(self.queryset.model, name=name)
        serializer = self.retrieve_serializer(instance)
        return Response(serializer.data)

    @detail_route(methods=['get'], url_name='detail-full')
    def detail(self, request, name=None):
        instance = get_object_or_404(self.queryset.model, name=name)
        serializer = self.detail_serializer(instance)
        return Response(serializer.data)


class CityViewSet(BaseGeoViewSet):
    """Class containing city related views."""
    queryset = City.objects.all()
    retrieve_serializer = serializers.SimpleCitySerializer
    detail_serializer = serializers.FullCitySerializer


class CountryViewSet(BaseGeoViewSet):
    """Class contains country related views."""
    queryset = Country.objects.all()
    retrieve_serializer = serializers.SimpleCountrySerializer
    detail_serializer = serializers.FullCountrySerializer
