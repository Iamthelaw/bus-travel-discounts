"""
Command for cleaning up database
---------------------------------------

Clean database from old discounts that no longer available.
I plan to run it once a week as this project goes live.

Run command:

.. code-block:: console

    $ django-admin cleanup
"""
from django.core.management.base import BaseCommand

from discount.models import Discount
from geo_data.models import Country


class Command(BaseCommand):
    """Remove garbage."""
    help = 'Remove garbage from database'

    def handle(self, *args, **options):
        """Removes garbage."""
        # Remove discounts that no longer active
        Discount.objects.filter(is_active=False).delete()
        # Remove Countries without cities
        Country.objects.filter(cities__isnull=True).delete()
