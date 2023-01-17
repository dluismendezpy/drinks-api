from django.contrib import admin
from django.urls import include, path
from drf_yasg.openapi import Contact, Info, License
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view: type = get_schema_view(
    Info(
        title="Drinks API",
        default_version="v1",
        description="Drinks API documentation",
        terms_of_service="https://luismendezdev.com",
        contact=Contact(name="Luis Mendez", email="info@luismendezdev.com"),
        license=License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/",
        include(
            [
                path("core/", include("core.urls")),
                path("drink/", include("drink.urls")),
                path(
                    "docs/",
                    include(
                        [
                            path(
                                "s/",
                                schema_view.with_ui(
                                    "swagger", cache_timeout=0
                                ),
                                name="swagger",
                            ),
                            path(
                                "r/",
                                schema_view.with_ui("redoc", cache_timeout=0),
                                name="redoc",
                            ),
                        ]
                    ),
                ),
            ]
        ),
    ),
]
