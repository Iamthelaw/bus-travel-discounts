# encoding: utf-8
from django.db import models

from geo_data.models import City


class TimelessManager(models.Manager):
    def get_queryset(self):
        return (
            super(TimelessManager, self)
                .get_queryset()
                .filter(
                    time_start__isnull=True,
                    time_end__isnull=True
                )
        )


class PricelessManager(models.Manager):
    def get_queryset(self):
        return (
            super(PricelessManager, self)
                .get_queryset()
                .filter(price__lte=0)
        )


class Currency(models.Model):
    """Currency implementation."""
    code = models.CharField(max_length=3)
    symbol = models.CharField(max_length=1)


class Discount(models.Model):
    """Discount implementation."""
    from_city = models.ForeignKey(City, related_name='discount_from_city')
    to_city = models.ForeignKey(City, related_name='discount_to_city')

    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=8)
    currency = models.ForeignKey(Currency)

    time_start = models.DateField(null=True, blank=True)
    time_end = models.DateField(null=True, blank=True)

    objects = models.Manager()
    timeless =  TimelessManager()
    priceless = PricelessManager()