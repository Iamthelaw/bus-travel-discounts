"""ecolinesdiscounts URLs main configuration file."""
import os

from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """SPA-app index view."""
    template_name = 'index.html'


urlpatterns = [
    url(r'^%s/' % os.environ.get('ADMIN_URL', 'admin'), admin.site.urls),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    # url(r'^api/v1/', include('discount.urls')),
    url(r'^api/v1/', include('geo_data.urls')),
    # All other urls go to SPA app
    # url(r'', IndexView.as_view()),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
