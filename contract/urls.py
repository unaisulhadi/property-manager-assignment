from django.urls import path

from .views import ContractListCreateAPIView

urlpatterns = [
    path(
        "contracts/", ContractListCreateAPIView.as_view(), name="contract-list-create"
    ),
]
