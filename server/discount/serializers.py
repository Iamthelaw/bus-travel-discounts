"""Django rest framework serializers for the discount app."""
from rest_framework import serializers

from discount.models import Discount


class DiscountSerializer(serializers.ModelSerializer):
    """Discount model serializer."""
    from_city = serializers.SlugRelatedField(read_only=True, slug_field='name')
    to_city = serializers.SlugRelatedField(read_only=True, slug_field='name')
    original_currency = serializers.SlugRelatedField(
        read_only=True, slug_field='code')

    class Meta:
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
