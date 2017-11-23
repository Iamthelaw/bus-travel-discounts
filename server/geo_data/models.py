"""Models definitions for geo data app."""
from django.db import models


class Country(models.Model):
    """Country model."""
    name = models.CharField(max_length=250, unique=True)
    #: International 2 characters code of country
    #: here used for drawing country flags on frontend
    code = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """I want to be sure that code is in upper case."""
        self.code = self.code and self.code.upper()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('name', )


class City(models.Model):
    """City model."""
    name = models.CharField(max_length=250, unique=True)
    country = models.ForeignKey(Country, related_name='cities')
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)

    @property
    def pretty_name(self):
        """Returns selected variant name."""
        main_variant = self.variants.filter(is_main=True)
        if main_variant.exists():
            return main_variant.first().name
        else:
            return self.variants.first().name

    def __str__(self):
        return '{}, {}'.format(self.pretty_name, self.country)

    class Meta:
        ordering = ('name', 'country')
        unique_together = (('name', 'country'), )


class Variant(models.Model):
    """Special model for different names of one city."""
    name = models.CharField(max_length=250)
    city = models.ForeignKey(City, related_name='variants')

    #: Used to set city name to one of variants
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return '{} ({}), {}'.format(
            self.name, self.city.name, self.city.country.name)

    class Meta:
        ordering = ('name', 'city')
        unique_together = (('name', 'city'), )
