"""REST views for discount app."""
from copy import copy
from itertools import groupby

from rest_framework.decorators import api_view
from rest_framework.response import Response

from geo_data.models import Country
from discount.models import Discount
from discount.serializers import DiscountSerializer


def pretty_result(discount_item):
    """Formats output a little."""
    return {
        'from_city': discount_item['from_city__name'],
        'to_city': discount_item['to_city__name'],
        'original_price': discount_item['original_price'],
        'original_currency': discount_item['original_currency__code'],
        'link': discount_item['link'],
    }


@api_view(['GET'])
def top(request):
    """Top 10 discounts."""
    if request.method == 'GET':
        discounts = Discount.objects.filter(is_active=True)[:10]
        serializer = DiscountSerializer(discounts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def by_country(request):
    """All results grouped by country."""
    if request.method == 'GET':
        country_field = 'from_city__country__name'
        discounts = Discount.objects.filter(is_active=True).order_by(
            'from_city__country', 'from_city', 'to_city').values(
                country_field,
                'from_city__name',
                'to_city__name',
                'original_price',
                'original_currency__code',
                'link',
        )
        result = {}
        for group_name, items in groupby(discounts, lambda x: x[country_field]):
            result[group_name] = tuple(pretty_result(item) for item in items)
        return Response(result)

