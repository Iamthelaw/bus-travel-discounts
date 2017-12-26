"""
Parser command
--------------
"""
from django.core.management.base import BaseCommand

from parser.ecolines import LocalUrlParser
from parser.ecolines import OfferPageParser


class Command(BaseCommand):
    """
    Command to start parser.

    .. code-block:: console

        django-admin parser
    """
    help = 'Parse and store info in database'

    def __init__(self, use_timeout, *args, **kwargs):
        self.parser = OfferPageParser(use_timeout=use_timeout)
        self.localized_links = LocalUrlParser(use_timeout=use_timeout)()
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        for link in self.localized_links:
            self.parser.url = link
            self.parser()
