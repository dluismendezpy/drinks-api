from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import DrinkAction, DrinkList

urlpatterns = [
    path("", DrinkList.as_view(), name="drink_list"),
    path("<int:pk>/", DrinkAction.as_view(), name="drink_actions"),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=["json", "html"])
