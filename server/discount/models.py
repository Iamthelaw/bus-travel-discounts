"""Model classes for discounts app."""
from django.db import models

from geo_data.models import City
from money.models import Currency


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
    parser = models.CharField(max_length=200, default='UnknownParser')

    #: See management command to clean-up database
    is_active = models.BooleanField(default=True)

    @property
    def from_country_code(self):
        """Code for beginning country."""
        return self.from_city.country.code

    @property
    def to_country_code(self):
        """Code for destination country."""
        return self.to_city.country.code

    def price(self):
        """Formatted original price."""
        return '{} {}'.format(self.original_price, self.original_currency.code)

    def __str__(self):
        return '{} → {}'.format(self.from_city.name, self.to_city.name)

    class Meta:
        ordering = ('from_city', 'to_city')
        unique_together = (('from_city', 'to_city'), )
