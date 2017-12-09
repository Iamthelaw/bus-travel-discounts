"""
Ecolines parser
===============
"""
import json
from decimal import Decimal

from parser.base import BaseParser

from geo_data.proxy import CityProxy
from money.models import Currency

DOMAIN = 'http://ecolines.net'
SEPARATOR_SYMBOL = '→'
LANGUAGE = 'ecolines_language'
LOCALIZATION = 'localization'


class EcolinesParser(BaseParser):
    """
    Ecolines parser class.

    Example usage:

    .. code-block:: python

        parser = EcolinesParser(
            offers={'class_': 'offer'},
            destinations={'class_': 'offer-title'},
            price={'name': 'span', 'class_': 'label'},
            link={'class_': 'offer-link'},
        )
        parser.run()
    """

    def _link_to_deals_page(self, url):
        """Local method for extracting link to special deals page."""
        soup = self.soup(url)
        link = tuple(soup.find(id='main-navbar').find_all('li'))[1]
        return DOMAIN + link.find('a').get('href')

    def _urls(self):
        """Dirty method, needs a lot of love and refactoring."""
        template = DOMAIN + '/{}/{}'

        soup = self.soup(DOMAIN)
        scripts = (_.get_text() for _ in soup.find_all('script'))
        inlined_javascript = tuple(_ for _ in scripts if LANGUAGE in _)[-1]
        if not inlined_javascript:
            print('no listing found')
        inlined_javascript = json.loads(
            inlined_javascript
            .replace('jQuery.extend(Drupal.settings, ', '')
            .replace(');', '')
        )
        localization = inlined_javascript[LANGUAGE][LOCALIZATION]
        for region, data in json.loads(localization).items():
            languages = data['lng']
            for lang in languages:
                yield self._link_to_deals_page(template.format(region, lang))

    @staticmethod
    def _cleanup_destinations(tag):
        destinations = tag.get_text().split(SEPARATOR_SYMBOL)
        if len(destinations) == 1:
            destinations = destinations[0].split('-')[:2]
        from_, to_ = tuple(_.strip() for _ in destinations)[:2]
        return CityProxy(from_).get(), CityProxy(to_).get()

    @staticmethod
    def _cleanup_price(tag):
        data = tag.get_text().split()
        price, currency = data[:-1], data[-1]
        price = ''.join(price).replace(',', '.').replace(' ', '')
        try:
            price = Decimal(price)
        except (ValueError, AttributeError):
            price = 0
        currency, _ = Currency.objects.get_or_create(
            code=currency.upper()[:3])
        return price, currency

    @staticmethod
    def _cleanup_link(tag):
        return tag.get('href')
