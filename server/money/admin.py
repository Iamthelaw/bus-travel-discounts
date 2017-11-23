"""Admin classes for discounts models"""
from django.contrib import admin

from money.models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    """Admin class for Currency model."""
    search_fields = ('code', )
