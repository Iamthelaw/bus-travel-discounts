"""
Api views
=========
"""
from itertools import groupby

from rest_framework.decorators import api_view
from rest_framework.response import Response

from discount.models import Discount
from discount.serializers import DiscountSerializer


def pretty_result(discount_item):
    """
    Formats output a little to hold expected api desined concept.
    """
    # TODO Need to find a way to do it in serializer
    # instead of this
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
    # FIXME This pile of garbage needs refactor ASAP
    if request.method == 'GET':
        country_name = 'from_city__country__name'
        discounts = Discount.objects.filter(is_active=True).order_by(
            'from_city__country', 'from_city', 'to_city').values(
                country_name,
                'from_city__name',
                'to_city__name',
                'original_price',
                'original_currency__code',
                'link')
        result = {}
        for group_name, items in groupby(discounts, lambda x: x[country_name]):
            result[group_name] = tuple(pretty_result(item) for item in items)
        return Response(result)
