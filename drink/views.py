from django.db.models import QuerySet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import Drink
from .serializers import DrinkSerializer


@api_view(["GET"])
def drink_api_view(request):
    if request.method == "GET":
        drinks: QuerySet | QuerySet[Drink] = Drink.objects.all().values(
            "id", "name", "description", "is_available"
        )
        drink_serializer: DrinkSerializer = DrinkSerializer(drinks, many=True)
        return Response({"drinks": drink_serializer.data}, status=HTTP_200_OK)
