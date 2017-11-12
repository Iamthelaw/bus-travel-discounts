"""Models definitions for geo data app."""
from django.db import models


class Country(models.Model):
    """Country model."""
    name = models.CharField(max_length=250, unique=True)


class City(models.Model):
    """City model."""
    name = models.CharField(max_length=250, unique=True)
    country = models.ForeignKey(
        Country, related_name='cities')
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        unique_together = (('name', 'country'), )


class Variant(models.Model):
    """Special model for different names of one city."""
    name = models.CharField(max_length=250)
    city = models.ForeignKey(City)

    class Meta:
        unique_together = (('name', 'city'), )
