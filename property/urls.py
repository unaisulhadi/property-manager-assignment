from django.urls import path

from .views import PropertyListAPIView

urlpatterns = [
    path('properties/', PropertyListAPIView.as_view(), name='property-list'),
]