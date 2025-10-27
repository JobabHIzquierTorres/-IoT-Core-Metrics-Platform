from rest_framework.routers import DefaultRouter

from .views import MetricViewSet

# Endpoint

router = DefaultRouter()
router.register(r"metrics", MetricViewSet)

urlpatterns = router.urls
