"""
Abstract base class
===================

Mother of all parsers, that *can* be made in future.
"""
import time
import warnings

import requests
from django.conf import settings
from bs4 import BeautifulSoup

from .exceptions import RequestError


class Parser:
    """
    Base class for parsers.

    This class is responsible for requests and passing reslts tp
    :class:`BeauifulSoup`.
    """
    def __init__(self, use_timeout=True):
        self.raw_html = None
        self.collected_data = set()
        self.use_timeout = use_timeout

    def harvest(self, page_url):
        """Get all that data from url."""
        # When testing I dont need timeout at all
        if self.use_timeout:
            time.sleep(settings.REQUESTS_TIMEOUT)
        response = requests.get(page_url)
        if response.status_code == 200:
            self.raw_html = response.content
            return response
        raise RequestError('Can\'t connect to the server! %s' % page_url)

    @property
    def soup(self):
        """Just serves soup from html."""
        if self.raw_html is None:
            warnings.warn(
                'Probably you did not call harvest before soup')
        return BeautifulSoup(self.raw_html, 'html.parser')
