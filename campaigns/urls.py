from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, CampaignMetricViewSet, CreativeAssetViewSet

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet)
router.register(r'metrics', CampaignMetricViewSet)
router.register(r'assets', CreativeAssetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
