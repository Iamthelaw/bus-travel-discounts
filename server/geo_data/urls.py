"""Url endpoints for geo_data app."""
from django.urls import path

from geo_data import views


urlpatterns = [
    path('city/<slug:city_name>/', views.city),
    path('city/<slug:city_name>/', views.city_details),
    path('country/<slug:country_name>/', views.country),
    path('country/<slug:country_name>/', views.country_details),
]
