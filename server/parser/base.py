"""
Abstract base class
===================

Mother of all parsers, that *can* be made in future.
"""
import time
import logging
from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup

from discount.proxy import DiscountProxy
from discount.models import Discount

logger = logging.getLogger(__name__)


class BaseParser(ABC):
    """
    Abstract base class.

    Usage example

    .. code-block:: python

        class MyParser(BaseParser):

            def _urls(self):
                # Should return all urls for parsing
                return [
                    'http://example.com/ru/ru,
                    'http://example.com/en/us'
                ]

            def _cleanup_destinations(tag):
                # self.destinations is element selector
                # like 'span.offer-destinations'
                # Any cleanup processing is going here
                return tag.find(self.destinations)

            def _cleanup_price(tag):
                # Again any processing, cleanup, extraction
                # of price and currency from tag goes here
                return tag.find(self.price)

            def _cleanup_link(tag):
                return tag.find(self.link).attr('href')

    """
    def __init__(self, **kwargs):
        """Defining selectors."""
        self.offers = kwargs.get('offers')
        self.destinations = kwargs.get('destinations')
        self.price = kwargs.get('price')
        self.link = kwargs.get('link')

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

    # TODO I should make this method overriding optional
    @staticmethod
    @abstractmethod
    def _cleanup_link(tag):
        """Extract link to original offer."""
        pass

    def process_offer(self, offer):
        """
        Process single offer.

        It runs overridden methods ``_cleanup_destinations``,
        ``_cleanup_price`` and ``_cleanup_link``, and then, from
        collected data returns object similar to this:

        .. code-block:: python

            {
                'from_city': 'Riga',
                'to_city': 'Moscow',
                'original_price': '5.14',
                'original_currency': 'EUR',
                'link': 'http://example.com/en/us/special-offer',
                'parser': 'MyParser'
            }

        """
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

    # TODO Do I really need this method?
    @staticmethod
    def soup(url):
        """Get a nice, tasty html soup."""
        response = requests.get(url)
        return BeautifulSoup(response.content, 'html.parser')

    def run(self):
        """
        Starts parsing process.

        First, it sets all discounts that are currently in database
        to state `is_active=False`

        Next, it collects urls for parsing from ``._urls()`` method

        Then starts parsing cycle. For every url:

        1. Create soup from raw html
        2. Get offers tags via ``self.offers`` selector
        3. Pass every process tag to ``.process_offer`` method

            1. Create proxy from data that was returned from
                ``.process_offfer`` method
            2. Get discount instance from proxy class. The instance is updated
                with info that we pass to proxy class.
            3. Set discount instance as active and continue to next offer
        """
        # Resets state of all discounts in database
        Discount.objects.all().update(is_active=False)
        urls = self._urls()
        for url in urls:
            logger.info(url)
            soup = self.soup(url)
            for offer in soup.find_all(**self.offers):
                kwargs = self.process_offer(offer)
                proxy = DiscountProxy(kwargs)
                discount = proxy.get()
                discount.is_active = True
                discount.save()
            # TODO I should probably move this to project settings
            # We don't want to be rude
            time.sleep(5)
