from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from core.response import SuccessResponse, ErrorResponse

from .serializer import PropertySerializer, UnitSerializer
from .models import Property, Unit


class PropertyListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PropertySerializer

    def get_queryset(self):
        return Property.objects.all()

    def get(self, request):
        properties = self.get_queryset()
        serializer = self.get_serializer(properties, many=True)
        return SuccessResponse(
            message="Properties fetched successfully", data=serializer.data
        )

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(
                message="Property created successfully", data=serializer.data
            )
        return ErrorResponse(
            message="Property creation failed", errors=serializer.errors
        )


class PropertyRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PropertySerializer

    def get_queryset(self):
        return Property.objects.all()

    def get(self, request, *args, **kwargs):
        property = self.get_object()
        serializer = self.get_serializer(property)
        return SuccessResponse(
            message="Property fetched successfully", data=serializer.data
        )


class UnitListByPropertyCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UnitSerializer

    def get_queryset(self):
        return Unit.objects.filter(property=self.kwargs["pk"])

    def get(self, request, *args, **kwargs):
        units = self.get_queryset()
        serializer = self.get_serializer(units, many=True)
        return SuccessResponse(
            message="Units fetched successfully", data=serializer.data
        )

    def post(self, request, *args, **kwargs):
        request.data["property"] = self.kwargs["pk"]
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(
                message="Unit created successfully", data=serializer.data
            )
        return ErrorResponse(message="Unit creation failed", errors=serializer.errors)


class ListAllUnitsAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UnitSerializer

    def get_queryset(self):
        return Unit.objects.all()

    def get(self, request, *args, **kwargs):
        units = self.get_queryset()
        status = request.query_params.get("status", None)
        if status:
            units = units.filter(status=status)
        serializer = self.get_serializer(units, many=True)
        return SuccessResponse(
            message="Units fetched successfully", data=serializer.data
        )
