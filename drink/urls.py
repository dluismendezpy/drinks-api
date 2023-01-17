from django.urls import path

from .views import drink_api_view

urlpatterns = [
    path("", drink_api_view, name="get_drinks"),
]
