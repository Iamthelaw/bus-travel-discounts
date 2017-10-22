# encoding: utf-8
from django.contrib import admin

from geo_data.models import City, Country


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass