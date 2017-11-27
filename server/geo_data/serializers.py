"""Geo serializers."""
from rest_framework import serializers, fields

from discount.serializers import DiscountSerializer
from geo_data.models import City
from geo_data.models import Country


class SimpleCountrySerializer(serializers.ModelSerializer):
    """General information about country."""
    cities = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='name')

    class Meta:
        model = Country
        fields = ('name', 'code', 'cities')


class SimpleCitySerializer(serializers.ModelSerializer):
    """General information about the city"""
    country = SimpleCountrySerializer()

    class Meta:
        model = City
        fields = ('name', 'country', 'latitude', 'longitude')


class FullCitySerializer(SimpleCitySerializer):
    """City information plus discounts related to city."""
    discounts = fields.SerializerMethodField()

    def get_discounts(self, city):
        """Returns all discounts related to city."""
        return {
            'from_city': DiscountSerializer(
                city.discount_from_city.all(), many=True).data,
            'to_city': DiscountSerializer(
                city.discount_to_city.all(), many=True).data,
        }

    class Meta:
        model = City
        fields = ('name', 'latitude', 'longitude', 'discounts')


class FullCountrySerializer(SimpleCountrySerializer):
    """General information about country."""
    cities = fields.SerializerMethodField()

    def get_cities(self, country):
        """Returns all cities discounts for country."""
        return FullCitySerializer(country.cities.all(), many=True).data

    class Meta:
        model = Country
        fields = ('name', 'code', 'cities')

