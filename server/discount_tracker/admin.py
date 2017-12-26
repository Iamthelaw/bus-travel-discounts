"""Django admin."""
from django.contrib import admin

from discount_tracker.models import CityTracker, CountryTracker


@admin.register(CityTracker)
class CityTrackerAdmin(admin.ModelAdmin):
    """Admin class for CityTracker model."""
    pass


@admin.register(CountryTracker)
class CountryTrackerAdmin(admin.ModelAdmin):
    """Admin class for CountryTracker model."""
    pass
