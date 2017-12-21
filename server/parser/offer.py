"""Offer managemenet."""
from decimal import Decimal

from discount.models import Discount
from money.models import Currency
from geo_data.proxy import CityProxy


class Destinations():
    """."""

    def __init__(self):
        self.separator = '→'

    def __get__(self, obj, objtype):
        if obj is None:
            return self
        return (obj.from_city, obj.to_city)

    def __set__(self, obj, val):
        destinations = val.split(self.separator)
        if len(destinations) == 1:
            destinations = destinations[0].split('-')[:2]
        destinations = tuple(
            _.strip() for _ in destinations
        )[:2]
        try:
            obj.from_city, obj.to_city = destinations
        except ValueError:
            obj.from_city, obj.to_city = destinations + (None, )


class Price():
    """."""

    def __get__(self, obj, objtype):
        if obj is None:
            return self
        return (obj.price, obj.currency)

    def __set__(self, obj, val):
        data = val.split()
        currency = None
        if len(data) == 1:
            price = data[0]
        else:
            try:
                price, currency = data[:-1], data[-1]
            except IndexError:
                obj.price = 0.
                obj.currency, _ = Currency.objects.get_or_create(code='XXX')
                return
        price = (
            ''.join(price)
            .replace(',', '.')
            .replace(' ', '')
        )
        try:
            price = Decimal(price)
        except (ValueError, AttributeError):
            price = 0
        currency, _ = Currency.objects.get_or_create(
            code=currency.upper()[:3] if currency else 'XXX')
        obj.currency = currency
        obj.price = price


class Link():
    """."""

    def __get__(self, obj, objtype):
        if obj is None:
            return self
        return obj.link

    def __set__(self, obj, val):
        obj.link = val


class Offer:
    """Offer class."""

    def __init__(self, use_timeout=True):
        self.from_city = None
        self.to_city = None
        self.price = None
        self.currency = None
        self.link = None
        self.use_timeout = use_timeout

    destinations = Destinations()
    price_tag = Price()
    link_tag = Link()

    def __str__(self):
        return '<Offer {} -> {}, {} {}>'.format(
            self.from_city,
            self.to_city or 'None',
            self.price or 0,
            self.currency and self.currency.code or 'None')

    def save(self):
        """."""
        from_city = CityProxy(
            self.from_city, use_timeout=self.use_timeout).get()
        to_city = CityProxy(
            self.to_city, use_timeout=self.use_timeout).get()
        offer, _ = Discount.objects.get_or_create(
            from_city=from_city,
            to_city=to_city
        )
        print(self.currency)
        offer.original_price = self.price
        offer.original_currency = self.currency
        offer.link = self.link
        return offer
