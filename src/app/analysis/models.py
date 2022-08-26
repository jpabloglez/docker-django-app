import uuid as uuid_lib
from django.conf import settings
from django.db import models
from core.models import TimeStampedModel

# Create your models here.

class Analysis(TimeStampedModel):
    """Analysis model"""
    service = models.CharField(max_length=24)
    description = models.TextField(blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='analyses')

    def __str__(self):
        return self.service

class Job(TimeStampedModel):
    """Job model"""
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    status = models.CharField(max_length=24)
    description = models.TextField(blank=True)
    analysis = models.ForeignKey(
        Analysis, on_delete=models.CASCADE, related_name='jobs')


    def __str__(self):
        return self.status