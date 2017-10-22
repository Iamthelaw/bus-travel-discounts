# encoding: utf-8
from django.contrib import admin

from discount.models import Currency, Discount


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass