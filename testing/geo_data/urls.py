"""Test api endpoints."""
import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_city_retrieve(client, city):
    res = client.get(reverse('city-detail', args=[city.name]))
    assert res.status_code == 200


@pytest.mark.django_db
def test_city_detail(client, city):
    res = client.get(reverse('city-detail-full', args=[city.name]))
    assert res.status_code == 200


@pytest.mark.django_db
def test_country_retrieve(client, city):
    res = client.get(reverse('country-detail', args=[city.country.name]))
    assert res.status_code == 200


@pytest.mark.django_db
def test_country_detail(client, city):
    res = client.get(reverse('country-detail-full', args=[city.country.name]))
    assert res.status_code == 200
