from rest_framework import serializers
from .models import Contract
from django.utils import timezone
from property.models import Unit
from django.db import transaction


class ContractSerializer(serializers.ModelSerializer):
    total_contract_value = serializers.SerializerMethodField(read_only=True)

    def validate(self, attrs):
        start_date = attrs.get("start_date")
        end_date = attrs.get("end_date")
        unit = attrs.get("unit")

        if start_date > end_date:
            raise serializers.ValidationError("Start date must be before end date")

        overlapping_contracts = Contract.objects.filter(
            unit=unit,
            start_date__lte=end_date,
            end_date__gte=start_date,
        )

        if overlapping_contracts.exists():
            raise serializers.ValidationError(
                "This unit is already booked for the selected date range"
            )

        return attrs

    def get_total_contract_value(self, obj):
        total_days = (obj.end_date - obj.start_date).days
        return float(obj.monthly_rent * total_days / 30)

    def _sync_unit_status(self, unit):
        today = timezone.now().date()
        has_active_contract = Contract.objects.filter(
            unit=unit,
            start_date__lte=today,
            end_date__gte=today,
        ).exists()

        unit.status = (
            Unit.UnitStatus.OCCUPIED
            if has_active_contract
            else Unit.UnitStatus.AVAILABLE
        )
        unit.save(update_fields=["status"])

    @transaction.atomic
    def create(self, validated_data):
        if "monthly_rent" not in validated_data:
            validated_data["monthly_rent"] = validated_data["unit"].monthly_rent
        contract = super().create(validated_data)
        self._sync_unit_status(contract.unit)
        return contract

    class Meta:
        model = Contract
        fields = "__all__"
        extra_kwargs = {
            "monthly_rent": {"required": False},
        }
