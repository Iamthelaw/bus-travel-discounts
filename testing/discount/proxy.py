"""Tests for discount proxy class."""
import pytest

from discount.proxy import DiscountProxy

from discount.models import Discount


@pytest.mark.django_db
def test_valid_kwargs(kwargs):
    """Just test that with valid input all works as expected."""
    DiscountProxy(kwargs).get()
    assert Discount.objects.count() == 1


@pytest.mark.django_db
def test_update_process(kwargs):
    """Testing update process of proxy."""

    # Creating first instance
    evil_empire = 'http://yandex.ru'
    DiscountProxy(kwargs).get()

    # Getting instance again
    kwargs.update(link=evil_empire, original_price=100)
    DiscountProxy(kwargs).get()

    # No new instances created
    assert Discount.objects.count() == 1

    # Attributes are changed
    assert Discount.objects.first().link == evil_empire
    assert Discount.objects.first().original_price == 100
