"""
Root url config
===============

This module stores root url configuration for project and imports url
declarations from other django apps.

.. code-block:: python

    url(r'^%s/' % os.environ.get('ADMIN_URL', 'admin'), admin.site.urls),

This part is where I try to be clever - declaring admin url from
enviroment variable so my project is more secure for outside world.
"""
import os

from django.urls import include, path
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

#: Hardcoded base api endpoint, maybe I should move it to project settings?
API_URL = 'api/v1/'


class IndexView(TemplateView):
    """
    SPA-app index view.

    Simple class-based view that serves only one template ``index.html``
    """
    template_name = 'index.html'


urlpatterns = [
    path(os.environ.get('ADMIN_URL', 'admin') + '/', admin.site.urls),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path(API_URL, include('discount.urls')),
    path(API_URL, include('geo_data.urls')),

    # All other urls go to SPA app
    path('', IndexView.as_view()),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
