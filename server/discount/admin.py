"""Admin classes for discounts models"""
from django.contrib import admin

from discount.models import Discount


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    """Admin class for Discount model."""
    search_fields = ('from_city', 'to_city')
    list_filter = ('is_active', 'from_city__country')
    list_display = ('__str__', 'price')
