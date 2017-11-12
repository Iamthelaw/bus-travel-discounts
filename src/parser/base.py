"""Base class for creating parsers."""
import time
import logging
from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup

from discount.proxy import DiscountProxy


class BaseParser(ABC):
    """Abstract base class for parsers."""
    def __init__(self, **kwargs):
        """Defining selectors."""
        self.offers = kwargs.get('offers')
        self.destinations = kwargs.get('destinations')
        self.price = kwargs.get('price')
        self.link = kwargs.get('link')
        self.log = logging.getLogger('parser')

    @abstractmethod
    def _urls(self):
        """Get sites for parsing."""
        pass

    @staticmethod
    @abstractmethod
    def _cleanup_destinations(tag):
        """Extract destinations."""
        pass

    @staticmethod
    @abstractmethod
    def _cleanup_price(tag):
        """Extract price and currency."""
        pass

    @staticmethod
    @abstractmethod
    def _cleanup_link(tag):
        """Extract link to original offer."""
        pass

    def process_offer(self, offer):
        """Process single offer."""
        from_, to_ = self._cleanup_destinations(
            offer.find(**self.destinations))
        price, curr = self._cleanup_price(
            offer.find(**self.price))
        link = self._cleanup_link(offer.find(**self.link))
        return {
            'from_city': from_,
            'to_city': to_,
            'original_price': price,
            'original_currency': curr,
            'link': link,
            'parser': self.__class__.__name__
        }

    @staticmethod
    def soup(url):
        """Get a nice, tasty html soup."""
        response = requests.get(url)
        return BeautifulSoup(response.content, 'html.parser')

    def run(self):
        """It runs it all."""
        urls = self._urls()
        for url in urls:
            self.log.info(url)
            soup = self.soup(url)
            for offer in soup.find_all(**self.offers):
                kwargs = self.process_offer(offer)
                self.log.debug(kwargs)
                proxy = DiscountProxy(kwargs)
                proxy.get()
            # We don't want to be rude
            time.sleep(5)
