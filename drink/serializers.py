from rest_framework.serializers import ModelSerializer

from .models import Drink


class DrinkSerializer(ModelSerializer):
    """Serializer for Drink model"""

    class Meta:
        model = Drink
        fields = ("id", "name", "description", "is_available")
