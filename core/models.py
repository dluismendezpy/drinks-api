from django.db import models


class BaseModel(models.Model):
    """Base model"""

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> models.CharField:
        return self.name
