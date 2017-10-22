from django.contrib import admin

from discount_tracker.models import CityTracker, CountryTracker


@admin.register(CityTracker)
class CityTrackerAdmin(admin.ModelAdmin):
    pass


@admin.register(CountryTracker)
class CountryTrackerAdmin(admin.ModelAdmin):
    pass