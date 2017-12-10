import pytest

from geo_data.models import City, Country


@pytest.fixture()
def city():
    country = Country.objects.create(name='Latvia', code='LV')
    return City.objects.create(name='Riga', country=country)
