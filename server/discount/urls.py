"""Url endpoints for discount app."""
from django.urls import path

from discount import views


urlpatterns = [
    path('discount/top/', views.top),
    path('discount/by-country/', views.by_country),
]
