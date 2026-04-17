from django.contrib import admin

from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "unit",
        "member",
        "start_date",
        "end_date",
        "monthly_rent",
    )
    list_filter = ("unit", "member", "start_date", "end_date")
