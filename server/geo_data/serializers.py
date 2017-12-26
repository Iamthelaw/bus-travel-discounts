"""
Model serializers
=================
"""
from rest_framework import serializers, fields

from discount.serializers import DiscountSerializer
from geo_data.models import City
from geo_data.models import Country


class SimpleCountrySerializer(serializers.ModelSerializer):
    """
    General information about country.

    ``serializer.data`` returns output like this

    .. code-block:: json

        {
            "name": "Latvai",
            "code": "LV",
            "cities": [
                {
                    "name": "Riga"
                }
            ]
        }
    """
    cities = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='name')

    class Meta:
        """Serializer meta class."""
        model = Country
        #: Fields to return in output
        fields = ('name', 'code', 'cities')


class SimpleCitySerializer(serializers.ModelSerializer):
    """
    General information about the city.

    .. code-block:: json

        {
            "name": "Riga",
            "country": "Latvia",
            "latitude": "0.123123",
            "longitude": "1.123123"
        }
    """
    country = serializers.SlugRelatedField(
        read_only=True, slug_field='name')

    class Meta:
        """Serializer meta class."""
        model = City
        #: Fields to return in output
        fields = ('name', 'country', 'latitude', 'longitude')


class FullCitySerializer(SimpleCitySerializer):
    """
    City information plus discounts related to city.

    .. code-block:: json

        {
            "name": "Riga",
            "latitude": "0.123123",
            "longitude": "1.123123",
            "discounts": {
                "from_city": [],
                "to_city": []
            }
        }
    """
    discounts = fields.SerializerMethodField()

    @staticmethod
    def get_discounts(city):
        """Returns all discounts related to city."""
        return {
            'from_city': DiscountSerializer(
                city.discount_from_city.all(), many=True).data,
            'to_city': DiscountSerializer(
                city.discount_to_city.all(), many=True).data,
        }

    class Meta:
        """Serializer meta class."""
        model = City
        fields = ('name', 'latitude', 'longitude', 'discounts')


class FullCountrySerializer(SimpleCountrySerializer):
    """
    General information about country.

    The most expensive of them all

    .. code-block:: json

        {
            "name": "Latvia",
            "code": "LV",
            "cities": [
                {
                    "name": "Riga",
                    "latitude": "0.123123",
                    "longitude": "0.123123",
                    "discounts": {
                        "from_city": [],
                        "to_city": []
                    }
                }
            ]
        }
    """
    cities = fields.SerializerMethodField()

    @staticmethod
    def get_cities(country):
        """Returns all cities discounts for country."""
        return FullCitySerializer(country.cities.all(), many=True).data
