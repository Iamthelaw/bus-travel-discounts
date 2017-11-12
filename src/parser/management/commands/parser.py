"""Management command for parser."""
from parser.ecolines import EcolinesParser

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command to start parser."""
    help = 'Parse and store info in database'

    def handle(self, *args, **options):
        parser = EcolinesParser(
            offers={'class_': 'offer'},
            destinations={'class_': 'offer-title'},
            price={'name': 'span', 'class_': 'label'},
            link={'class_': 'offer-link'},
        )
        parser.run()
