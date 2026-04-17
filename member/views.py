from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializer import MemberSerializer
from .models import Member
from core.response import SuccessResponse, ErrorResponse


class MemberListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MemberSerializer

    def get_queryset(self):
        return Member.objects.all()

    def get(self, request, *args, **kwargs):
        members = self.get_queryset()
        serializer = self.get_serializer(members, many=True)
        return SuccessResponse(
            message="Members fetched successfully", data=serializer.data
        )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(
                message="Member created successfully", data=serializer.data
            )
        return ErrorResponse(message="Member creation failed", errors=serializer.errors)
