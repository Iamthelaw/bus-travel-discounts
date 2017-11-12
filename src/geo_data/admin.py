"""Django admin."""
from django.contrib import admin

from geo_data.models import City, Country


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """Admin class for City model."""
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """Admin class for Country model."""
    pass
