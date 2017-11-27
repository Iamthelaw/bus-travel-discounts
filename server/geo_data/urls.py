"""Url endpoints for geo_data app."""
from django.conf.urls import url

from geo_data import views


urlpatterns = [
    url(r'city/(?P<city_name>\w+)/$', views.city),
    url(r'city/(?P<city_name>\w+)/$', views.city_details),
    url(r'country/(?P<country_name>\w+)/$', views.country),
    url(r'country/(?P<country_name>\w+)/$', views.country_details),
]
