# encoding: utf-8
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=250)


class City(models.Model):
    name = models.CharField(max_length=250)
    country = models.OneToOneField(Country)