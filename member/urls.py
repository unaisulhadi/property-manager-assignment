from django.urls import path

from .views import MemberListCreateAPIView

urlpatterns = [
    path("members/", MemberListCreateAPIView.as_view(), name="member-list-create"),
]
