from django.contrib import admin

from .models import Property, Unit, Member, Contract


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    search_fields = ('name',)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'property',
        'unit_number',
        'monthly_rent',
        'status',
    )
    list_filter = ('property',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email')


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'unit',
        'member',
        'start_date',
        'end_date',
        'monthly_rent',
    )
    list_filter = ('unit', 'member', 'start_date', 'end_date')