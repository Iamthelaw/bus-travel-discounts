"""
Ecolines parser
===============
"""
import json

from parser.base import Parser

from .exceptions import ParserError
from .offer import Offer


class LocalUrlParser(Parser):
    """
    Collect location specific urls from international site.

    >>> localized_links = LocalUrlParser()()
    """

    domain = 'http://ecolines.net'
    language = 'ecolines_language'
    localization = 'localization'

    @property
    def locales(self):
        """Extracts locales from javascript part of the page."""
        scripts = (_.get_text() for _ in self.soup.find_all('script'))
        inlined_javascript = tuple(
            _ for _ in scripts if self.language in _
        )[-1]
        if not inlined_javascript:
            ParserError('Failed to find links to discounts!')
        inlined_javascript = json.loads(
            inlined_javascript
            .replace('jQuery.extend(Drupal.settings, ', '')
            .replace(');', '')
        )
        return inlined_javascript[self.language][self.localization]

    def __call__(self):
        self.harvest(self.domain)
        for region, data in json.loads(self.locales).items():
            languages = data['lng']
            for lang in languages:
                self.collected_data.add('/'.join((self.domain, region, lang)))


class OfferPageParser(Parser):
    """
    Collects data from offers page.

    >>> OfferPageParser('http://some-url.com')()
    """

    url = None

    @property
    def link_to_discounts(self):
        """Returns link to discounts page from site menu."""
        self.harvest(self.url)
        _, menu_item, *_ = tuple(
            self.soup.find(id='main-navbar').find_all('li')
        )
        return self.url + menu_item.find('a').get('href')

    def collect(self):
        """Store collected data in class attribute."""
        self.harvest(self.link_to_discounts)
        for tag in self.soup.find_all(class_='offer'):
            offer = Offer(use_timeout=self.use_timeout)
            offer.destinations = tag.find(
                class_='offer-title').get_text()
            offer.price_tag = tag.find(
                name='span', class_='label').get_text()
            offer.link_tag = tag.find(class_='offer-link').get('href')
            self.collected_data.add(offer)

    def __call__(self):
        self.collect()
        for offer in self.collected_data:
            offer.save()
