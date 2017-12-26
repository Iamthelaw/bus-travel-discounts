"""
Rest serializers
================
"""
from rest_framework import serializers

from discount.models import Discount


class DiscountSerializer(serializers.ModelSerializer):
    """
    Discount model serializer.

    Fields implemented with read-only access
    (:class:`rest_framework.serializers.SlugRelatedField`)
    to related models are:

    * ``from_city``
    * ``to_city``
    * ``original_currency``

    example ``serializer.data``:

    .. code-block:: json

        {
            "from_city": "Riga",
            "from_country_code": "LV",
            "to_city": "Moscow",
            "to_country_code": "RU",
            "original_price": 12,
            "original_currency": "EUR",
            "link": "http://ecolines.es/ee/ru/discount"
        }
    """
    from_city = serializers.SlugRelatedField(read_only=True, slug_field='name')
    to_city = serializers.SlugRelatedField(read_only=True, slug_field='name')
    original_currency = serializers.SlugRelatedField(
        read_only=True, slug_field='code')

    class Meta:
        """Serializer meta class."""
        model = Discount
        fields = (
            'from_country_code',
            'from_city',
            'to_country_code',
            'to_city',
            'original_price',
            'original_currency',
            'link',
        )
