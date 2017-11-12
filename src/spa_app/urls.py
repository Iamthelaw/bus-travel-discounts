"""Url declaration."""
from django.conf.urls import url

from spa_app.views import index

urlpatterns = [
    url(r'', index),
]
