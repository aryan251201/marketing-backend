from django.db import models
from accounts.models import User

class Campaign(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CampaignMetric(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='metrics')
    date = models.DateField()
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    conversions = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.campaign.name} - {self.date}"
    

class CreativeAsset(models.Model):
    ASSET_TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('doc', 'Document'),
    )

    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='assets')
    file_url = models.TextField()
    asset_type = models.CharField(max_length=20, choices=ASSET_TYPE_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asset_type} for {self.campaign.name}"