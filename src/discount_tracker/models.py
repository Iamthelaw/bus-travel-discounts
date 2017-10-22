# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

from geo_data.models import City
from geo_data.models import Country


class BaseTracker(models.Model):
    """Abstract tracker implementation."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class CityTracker(BaseTracker):
    """Tracker specific to city relations."""
    from_city = models.ForeignKey(City, related_name='tracker_from_city')
    to_city = models.ForeignKey(City, related_name='tracker_to_city')


class CountryTracker(BaseTracker):
    """Tracker specific to country relations."""
    DIRECTION_CHOICES = (
        (0, 'from'),
        (10, 'to'),
        (20, 'all'),
    )
    country = models.ForeignKey(Country)
    direction = models.PositiveSmallIntegerField(choices=DIRECTION_CHOICES)