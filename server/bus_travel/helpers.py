"""
Helpers
=======

Here are definitions that commonly used in two or more django apps
"""
import unicodedata

from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response


# TODO This part needs another design decision!
def instance_view(model_serializer):
    """
    Generic instance details view.
    Basically only GET responses to data if it exists, if not - 404
    error will be raised.

    :param model_serializer: Serializer class for model

    :returns: wrapped in :func:`rest_framework.decorators.api_view`
        instance view function
    """
    @api_view(['GET'])
    def wrapper(request, instance_slug):
        """Wraps api_view and django view in onw function."""
        model_class = model_serializer.Meta.model
        model_instance = get_object_or_404(model_class, name=instance_slug)
        serializer = model_serializer(model_instance)
        return Response(serializer.data)
    return wrapper


# This is here because geo_data and service both need it
def serialize(text):
    """
    Cleanup any text (but designed for city names).

    Unfortunately, name of the city can contain special for European
    languages symbols - diacritics, that can interfere with
    geo(de)coding process.

    >>> serialize('The françois')
    'Francois'

    Can be extended with more ``.replace()`` calls if needed.
    Also decided that creating a variable for every
    processing steps will be a waste of resources.

    P.S. I love this clean representation of chained methods.
    Javascript is not ugly, but prejudices are.
    """
    if isinstance(text, str):
        return (
            unicodedata
            .normalize('NFD', text)
            .encode('ascii', 'ignore')
            .decode('utf-8')
            .replace('The ', '')
            .capitalize()
            .strip()
        )
    # Whatever it was, push it back if it wasn't a string
    return text
