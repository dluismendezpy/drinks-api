from django.db import models

from core.models import BaseModel


class Drink(BaseModel):
    """Drinks model"""

    is_available = models.BooleanField(
        default=True, help_text="Handle drink available in stock"
    )
