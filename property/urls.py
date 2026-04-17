from django.urls import path

from .views import (PropertyListCreateAPIView, PropertyRetrieveAPIView,
                    UnitListByPropertyCreateAPIView, ListAllUnitsAPIView)

urlpatterns = [
    # Property listing and creation
    path('properties/', PropertyListCreateAPIView.as_view(), name='property-list-create'),
    path('properties/<int:pk>/', PropertyRetrieveAPIView.as_view(), name='property-retrieve'),

    # Unit listing and creation
    path('properties/<int:pk>/units/', UnitListByPropertyCreateAPIView.as_view(), name='unit-create'),
    path('properties/units/', ListAllUnitsAPIView.as_view(), name='unit-list'),

]