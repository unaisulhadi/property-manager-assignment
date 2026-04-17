from django.contrib import admin

from .models import Property, Unit


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address")
    search_fields = ("name",)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "property",
        "unit_number",
        "monthly_rent",
        "status",
    )
    list_filter = ("property",)
