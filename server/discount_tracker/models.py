"""
Data models
===========
"""
from django.db import models
from django.contrib.auth.models import User

from geo_data.models import City
from geo_data.models import Country


class BaseTracker(models.Model):
    """
    Abstract tracker implementation.

    Really contains only one-to-one relation to user profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class CityTracker(BaseTracker):
    """
    Tracker specific for city relations.

    Holds two columns - **from_city** and **to_city**
    """
    from_city = models.ForeignKey(
        City, related_name='tracker_from_city', on_delete=models.CASCADE)
    to_city = models.ForeignKey(
        City, related_name='tracker_to_city', on_delete=models.CASCADE)


class CountryTracker(BaseTracker):
    """
    Tracker specific for country relations.

    It differs from city tracker in that it tracks country name and
    desired destination:

    * from this country
    * to this country
    * all
    """
    DIRECTION_CHOICES = (
        (0, 'from'),
        (10, 'to'),
        (20, 'all'),
    )
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE)
    direction = models.PositiveSmallIntegerField(choices=DIRECTION_CHOICES)
