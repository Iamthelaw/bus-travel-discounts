"""Api endpoints."""
from rest_framework.routers import SimpleRouter

from .views import CityViewSet, CountryViewSet

router = SimpleRouter()
router.register(r'city', CityViewSet)
router.register(r'country', CountryViewSet)

urlpatterns = router.urls
