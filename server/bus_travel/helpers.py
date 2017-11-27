"""Helper functions."""
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response


def instance_view(model_serializer, query_by='name'):
    """Generic instance details view."""
    @api_view(['GET'])
    def wrapper(request, instance_slug):
        """Wraps api_view and django view in onw function."""
        model_class = model_serializer.Meta.model
        model_instance = get_object_or_404(model_class, name=instance_slug)
        serializer = model_serializer(model_instance)
        return Response(serializer.data)
    return wrapper
