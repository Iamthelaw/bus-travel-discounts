"""Test api endpoints."""
import json
import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_discount_list(client, discounts):
    res = client.get(reverse('discount-list'))
    assert res.status_code == 200
    res = json.loads(res.content)
    assert len(res) == 10
