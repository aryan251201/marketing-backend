from rest_framework import viewsets
from .models import Campaign, CampaignMetric, CreativeAsset
from .serializers import CampaignSerializer, CampaignMetricSerializer, CreativeAssetSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class CampaignMetricViewSet(viewsets.ModelViewSet):
    queryset = CampaignMetric.objects.all()
    serializer_class = CampaignMetricSerializer

class CreativeAssetViewSet(viewsets.ModelViewSet):
    queryset = CreativeAsset.objects.all()
    serializer_class = CreativeAssetSerializer
