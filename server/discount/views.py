"""
Api views
=========
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response

from discount.models import Discount
from discount.serializers import DiscountSerializer


@api_view(['GET'])
def top(request):
    """Top 10 discounts."""
    if request.method == 'GET':
        discounts = Discount.objects.filter(is_active=True)[:10]
        serializer = DiscountSerializer(discounts, many=True)
        return Response(serializer.data)
