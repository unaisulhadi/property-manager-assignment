from django.urls import path

from .views import PropertyListCreateAPIView

urlpatterns = [
    path('properties/', PropertyListCreateAPIView.as_view(), name='property-list-create'),
]