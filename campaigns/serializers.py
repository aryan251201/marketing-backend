from rest_framework import serializers
from .models import Campaign, CampaignMetric, CreativeAsset

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'

class CampaignMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignMetric
        fields = '__all__'

class CreativeAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreativeAsset
        fields = '__all__'
