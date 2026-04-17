from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.response import SuccessResponse, ErrorResponse

from .serializer import PropertySerializer
from .models import Property

class PropertyListAPIView(ListAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = PropertySerializer
    queryset = Property.objects.all()

