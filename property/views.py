from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from core.response import SuccessResponse, ErrorResponse

from .serializer import PropertySerializer
from .models import Property

class PropertyListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PropertySerializer

    def get_queryset(self):
        return Property.objects.all()

    def get(self, request):
        properties = self.get_queryset()
        serializer = self.get_serializer(properties, many=True)
        return SuccessResponse(message="Properties fetched successfully", data=serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(message="Property created successfully", data=serializer.data)
        return ErrorResponse(message="Property creation failed", errors=serializer.errors)

