# encoding: utf-8
"""Admin classes for discounts models"""
from django.contrib import admin

from discount.models import Currency, Discount


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    """Admin class for Currency model."""
    pass


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    """Admin class for Discount model."""
    pass
