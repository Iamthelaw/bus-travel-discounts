"""
Data models
===========
"""
from django.db import models


class Country(models.Model):
    """
    Data model for a country.
    """
    #: Country international name
    name = models.CharField(max_length=250, unique=True)
    #: International 2 characters country code
    #: here used for drawing country flags on frontend
    code = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Overwrite ``save`` method on a country model.

        Before saving changes to the database it ensures that country
        international code is in upper case.
        """
        self.code = self.code and self.code.upper()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('name', )


class City(models.Model):
    """Data model for a city."""
    # TODO Maybe this field can be removed, I can take city name from
    # main variant.
    #: I'm not sure that this field is necessary here
    name = models.CharField(max_length=250, unique=True)
    #: Link to country data model
    country = models.ForeignKey(
        Country, related_name='cities', on_delete=models.CASCADE)
    #: Geographical latitude
    latitude = models.CharField(max_length=100, null=True, blank=True)
    #: Geographical longitude
    longitude = models.CharField(max_length=100, null=True, blank=True)

    # TODO I think this can be easily replaced with ``name``
    @property
    def pretty_name(self):
        """
        Returns city name.

        If there is exists the main variant of city name it returns it.
        Else if there is one or some count of city variants names it
        returns first found city name variant.
        """
        main_variant = self.variants.filter(is_main=True)
        if main_variant.exists():
            return main_variant.first().name
        try:
            return self.variants.first().name
        except AttributeError:
            return self.name

    def __str__(self):
        return '{}, {}'.format(self.pretty_name, self.country)

    class Meta:
        ordering = ('name', 'country')
        unique_together = (('name', 'country'), )


class Variant(models.Model):
    """
    A data model that holds relations between cities and cities name variants.

    So the main idea of this is that city can have many names, and to be
    able to define main, most appropriate variant of city name we need this
    model.
    """
    #: Just a string representing a city
    name = models.CharField(max_length=250)
    #: Link to an actual city data model
    city = models.ForeignKey(
        City, related_name='variants', on_delete=models.CASCADE)

    #: Used to select this variant as the main variant of the city name
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return '{} ({}), {}'.format(
            self.name, self.city.name, self.city.country.name)

    class Meta:
        ordering = ('name', 'city')
        unique_together = (('name', 'city'), )
