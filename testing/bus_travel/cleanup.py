import pytest
import mimesis

from bus_travel.management.commands.cleanup import Command as CleanupCommand
from discount.models import Discount
from geo_data.models import City, Country


def country():
    country_name = mimesis.Address().country()
    if Country.objects.filter(name=country_name).exists():
        return country()
    return Country.objects.create(name=country_name)


def city(country):
    city_name = mimesis.Address().city()
    if City.objects.filter(name=city_name).exists():
        return city(country)
    return City.objects.create(name=city_name, country=country)


def make_offers(count=10, is_active=True):
    country_ = Country.objects.filter(cities__isnull=False).first()
    for _ in range(count):
        Discount.objects.create(
            from_city=city(country_),
            to_city=city(country_),
            is_active=is_active
        )


def make_countries(count=10, have_cities=True):
    for _ in range(count):
        if have_cities:
            country_ = country()
            city(country_)
        else:
            country()


@pytest.mark.django_db
def test_cleanup_command():
    make_countries(have_cities=False)
    make_countries()
    make_offers()
    make_offers(is_active=False)

    assert Discount.objects.count() == 20
    assert Country.objects.count() == 20
    CleanupCommand().handle()
    assert Country.objects.count() == 10
    assert not Country.objects.filter(cities__isnull=True).exists()
    assert Discount.objects.count() == 10
    assert not Discount.objects.filter(is_active=False).exists()
