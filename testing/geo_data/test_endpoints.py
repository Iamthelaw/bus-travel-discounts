"""Test api endpoints."""
import pytest

from django.urls import reverse

TEST_CITY = 'Riga'
TEST_COUNTRY = 'Latvia'


@pytest.mark.django_db
def test_city_retrieve(client, city):
    res = client.get(reverse('city-detail', args=[TEST_CITY]))
    assert res.status_code == 200


@pytest.mark.django_db
def test_city_detail(client, city):
    res = client.get(reverse('city-detail-full', args=[TEST_CITY]))
    assert res.status_code == 200


@pytest.mark.django_db
def test_country_retrieve(client, city):
    res = client.get(reverse('country-detail', args=[TEST_COUNTRY]))
    assert res.status_code == 200


@pytest.mark.django_db
def test_country_detail(client, city):
    res = client.get(reverse('country-detail-full', args=[TEST_COUNTRY]))
    assert res.status_code == 200
