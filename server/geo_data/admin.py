"""Django admin."""
from django.contrib import admin

from geo_data.models import City, Country, Variant


class VariantInline(admin.TabularInline):
    """City name variants."""
    model = Variant
    extra = 0


class CityInline(admin.TabularInline):
    """City belongs to Country."""
    model = City
    extra = 0


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    """Admin class for Variant model."""
    search_fields = ('name', )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """Admin class for City model."""
    search_fields = ('name', )
    inlines = [VariantInline]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """Admin class for Country model."""
    search_fields = ('name', )
    list_display = ('name', 'code')
    inlines = [CityInline]
