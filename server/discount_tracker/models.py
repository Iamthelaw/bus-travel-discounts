"""Models definitions for discount tracker app."""
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
    from_city = models.ForeignKey(
        City, related_name='tracker_from_city', on_delete=models.CASCADE)
    to_city = models.ForeignKey(
        City, related_name='tracker_to_city', on_delete=models.CASCADE)


class CountryTracker(BaseTracker):
    """Tracker specific to country relations."""
    DIRECTION_CHOICES = (
        (0, 'from'),
        (10, 'to'),
        (20, 'all'),
    )
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE)
    direction = models.PositiveSmallIntegerField(choices=DIRECTION_CHOICES)
