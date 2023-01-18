from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.views import APIView

from .models import Drink
from .serializers import DrinkSerializer


class DrinkList(APIView):
    """
    List all users, or create a new user.
    """

    @staticmethod
    def get(request: WSGIRequest, format=None) -> Response:
        """
        Get all drinks from DB
        :param WSGIRequest request: get request state info
        """
        drinks: QuerySet | QuerySet[Drink] = Drink.objects.all().values(
            "id", "name", "description", "is_available"
        )
        drinks_serializer: DrinkSerializer = DrinkSerializer(drinks, many=True)
        return Response({"drinks": drinks_serializer.data}, status=HTTP_200_OK)

    @staticmethod
    def post(request, format=None) -> Response:
        """
        Create new drink
        :param request: get request state info
        """
        drink_serializer: DrinkSerializer = DrinkSerializer(data=request.data)

        if drink_serializer.is_valid():
            drink_serializer.save()
            return Response(
                {"drinks": drink_serializer.data}, status=HTTP_201_CREATED
            )
        return Response(
            {"message": drink_serializer.errors}, status=HTTP_400_BAD_REQUEST
        )


class DrinkAction(APIView):
    """
    Get, update or delete a specific drink
    """

    @staticmethod
    def __get_drink(pk: int) -> Drink:
        """
        Try to get a specific Drink object or raise Http404
        :param pk: drink primary key
        """
        return get_object_or_404(Drink, pk=pk)

    def get(self, request, pk: int, format=None):
        """
        Get and expose a specific drink
        :param request: get request state info
        :param pk: drink primary key
        :param format: data format
        """
        drink: Drink = self.__get_drink(pk=pk)
        drink_serializer: DrinkSerializer = DrinkSerializer(drink)
        return Response({"drinks": drink_serializer.data}, status=HTTP_200_OK)

    def put(self, request, pk: int, format=None):
        """
        Update a specific Drink object
        :param request: get request state info
        :param pk: drink primary key
        :param format: data format
        """
        drink: Drink = self.__get_drink(pk=pk)
        drink_serializer = DrinkSerializer(drink, data=request.data)

        if drink_serializer.is_valid():
            drink_serializer.save()
            return Response(
                {"drinks": drink_serializer.data}, status=HTTP_200_OK
            )
        return Response(
            {"message": drink_serializer.errors}, status=HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk: int, format=None):
        """
        Delete a specific Drink object
        :param request: get request state info
        :param pk: drink primary key
        :param format: data format
        """
        drink: Drink = self.__get_drink(pk=pk)
        drink.delete()
        return Response(
            {"message": "Drink deleted successfully"}, status=HTTP_200_OK
        )
