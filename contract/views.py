from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.utils import timezone
from .serializer import ContractSerializer
from .models import Contract
from core.response import SuccessResponse, ErrorResponse


class ContractListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContractSerializer

    def get_queryset(self):
        queryset = Contract.objects.all()
        active_param = self.request.query_params.get("active")

        if active_param is None:
            return queryset

        active_value = active_param.strip().lower()
        today = timezone.now().date()

        if active_value == "true":
            return queryset.filter(start_date__lte=today, end_date__gte=today)

        if active_value == "false":
            return queryset.exclude(
                Q(start_date__lte=today) & Q(end_date__gte=today)
            )

        return queryset

    def get(self, request, *args, **kwargs):
        contracts = self.get_queryset()
        serializer = self.get_serializer(contracts, many=True)
        return SuccessResponse(
            message="Contracts fetched successfully", data=serializer.data
        )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(
                message="Contract created successfully", data=serializer.data
            )
        return ErrorResponse(
            message="Contract creation failed", errors=serializer.errors
        )
