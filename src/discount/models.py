"""Model classes for discounts app."""
from django.db import models

from geo_data.models import City


class Currency(models.Model):
    """Currency implementation."""
    code = models.CharField(max_length=3, unique=True)
    symbol = models.CharField(max_length=1)


class Discount(models.Model):
    """Discount implementation."""
    from_city = models.ForeignKey(City, related_name='discount_from_city')
    to_city = models.ForeignKey(City, related_name='discount_to_city')

    original_price = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=8)
    original_currency = models.ForeignKey(Currency)

    time_start = models.DateField(null=True, blank=True)
    time_end = models.DateField(null=True, blank=True)

    #: Who knows how long can be url string?
    link = models.TextField(blank=True)

    #: What parser created this record
    parser = models.CharField(max_length=200, default='AnknownParser')

    class Meta:
        unique_together = (('from_city', 'to_city'), )
