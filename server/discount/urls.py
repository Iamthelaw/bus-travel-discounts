"""Url endpoints for discount app."""
from django.conf.urls import url

from discount import views


urlpatterns = [
    url(r'discount/top/$', views.top),
    url(r'discount/by-country/$', views.by_country),
]