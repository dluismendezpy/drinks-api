from django.contrib import admin

from .models import Drink


@admin.action(description="Set available")
def make_users_staff(modeladmin, request, queryset):
    queryset.update(is_available=True)


@admin.action(description="Set not available")
def make_users_non_staff(modeladmin, request, queryset):
    queryset.update(is_available=False)


@admin.register(Drink)
class UserAdmin(admin.ModelAdmin):
    """Admin config for drink model"""

    fields = (
        "name",
        "description",
        "is_available",
        "created_at",
        "updated_at",
    )
    list_display = ("name", "description", "is_available")
    list_display_links = ("name",)
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("is_available", "created_at", "updated_at")
    ordering = ("-created_at",)
    actions = (make_users_staff, make_users_non_staff)
