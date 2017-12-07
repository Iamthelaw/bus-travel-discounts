"""
Proxy classes
=============
"""
from discount.models import Discount


class DiscountProxy(object):
    """Proxy class for getting discount instances."""

    def __init__(self, kwargs):
        self.fields_for_update = (
            'original_price',
            'original_currency',
            'link'
        )
        self.fields_for_filter = (
            'from_city',
            'to_city',
            'parser'
        )
        self.kwargs = kwargs

    def have_required_fields(self):
        """Check kwargs dictionary for required fields."""
        return all((key in self.kwargs for key in self.fields_for_filter))

    @property
    def instance(self):
        """Returns discount class instance."""
        try:
            discount = Discount.objects.get(
                from_city=self.kwargs['from_city'],
                to_city=self.kwargs['to_city'],
                parser=self.kwargs['parser']
            )
        except Discount.DoesNotExist:
            discount = Discount.objects.create(**self.kwargs)
        return discount

    @property
    def updated(self):
        """Updated instance of discount."""
        discount = self.instance
        for attr in self.fields_for_update:
            if self.kwargs.get(attr):
                setattr(discount, attr, self.kwargs[attr])
        discount.save()
        return discount

    def get(self):
        """Get new or updated discount instance."""
        if not self.have_required_fields():
            raise ValueError(
                'Required fields: ' + ", ".join(self.fields_for_filter)
            )
        return self.updated
