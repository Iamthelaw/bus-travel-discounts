"""Url endpoints for discount app."""
from django.conf.urls import url

from discount import views


urlpatterns = [
    url(r'^top/$', views.top),
    url(r'^by-country/$', views.by_country),
]
