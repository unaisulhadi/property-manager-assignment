from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializer import ContractSerializer
from .models import Contract
from core.response import SuccessResponse, ErrorResponse


class ContractListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContractSerializer

    def get_queryset(self):
        return Contract.objects.all()

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
