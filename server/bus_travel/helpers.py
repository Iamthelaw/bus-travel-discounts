"""
Helpers
=======

Here are definitions that commonly used in two or more django apps
"""
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response


# TODO This part needs another design decision!
def instance_view(model_serializer, query_by='name'):
    """
    Generic instance details view.
    Basicly only GET responses with data if it is exists, if not - 404
    error will be raised.

    :param model_serializer: Serializer class for model

    :returns: wrapped in :func:`rest_framework.decorators.api_view`
        instance view function
    :rtype: decorated function
    """
    @api_view(['GET'])
    def wrapper(request, instance_slug):
        """Wraps api_view and django view in onw function."""
        model_class = model_serializer.Meta.model
        model_instance = get_object_or_404(model_class, name=instance_slug)
        serializer = model_serializer(model_instance)
        return Response(serializer.data)
    return wrapper
