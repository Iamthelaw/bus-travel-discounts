import pytest
import mimesis

from geo_data.models import City, Country


@pytest.fixture
def city_name():
    """Returns random city name."""
    return mimesis.Address().city()


@pytest.fixture
def country_name():
    """Returns random country name."""
    return mimesis.Address().country()


@pytest.fixture
def country_code():
    """Returns international country code."""
    return mimesis.Address().country_iso_code()[:2]


@pytest.fixture
def price():
    """Returns random number."""
    return mimesis.Numbers().digit()


@pytest.fixture
def currency_code():
    """Returns random currency."""
    return mimesis.Business().currency_iso_code()


@pytest.fixture
def page_url():
    """Returns random url."""
    return mimesis.Internet().home_page()


@pytest.fixture
def img_url():
    """Returns fake image url."""
    return mimesis.Internet().image_placeholder()


@pytest.fixture
def html():
    """Returns small random html block."""
    return mimesis.Structured().html()


@pytest.fixture
def riga():
    """Returns Riga city instance."""
    return City.objects.create(
        name='Riga',
        country=Country.objects.create(name='Latvia', code='LV'))


@pytest.fixture
def helsinki():
    """Returns Helsinki city instance."""
    return City.objects.create(
        name='Helsinki',
        country=Country.objects.create(name='Finland', code='FI'))


@pytest.fixture
def city(city_name, country_name, country_code):
    """Returns random city with."""
    country = Country.objects.create(name=country_name, code=country_code)
    return City.objects.create(name=city_name, country=country)


@pytest.fixture
def cities(country_name, country_code):
    """Returns queryset of cities in one country."""
    country = Country.objects.create(name=country_name, code=country_code)
    for _ in range(10):
        City.objects.create(name=mimesis.Address.city(), country=country)
    return City.objects.all()


@pytest.fixture
def geo_api_response(city_name, country_code, country_name):
    """Return opencage api fake response."""
    return {
        'results': [
            {
                'geometry': {
                    'lat': mimesis.Address().latitude(),
                    'lng': mimesis.Address().longitude(),
                },
                'components': {
                    'city': city_name,
                    'state': country_code,
                    'country': country_name,
                }
            }
        ],
        'total_results': 1
    }
