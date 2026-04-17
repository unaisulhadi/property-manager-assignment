import logging

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from account.serializers import (LoginResponseSerializer, LoginSerializer, RegisterSerializer)
from core.response import ErrorResponse, SuccessResponse
from core.utils import format_serializer_errors

logger = logging.getLogger("base_logger")


class LoginView(GenericAPIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            # Perform authentication
            user = authenticate(email=email, password=password)
            if user is None:
                return ErrorResponse(
                    message="Authentication failed",
                    errors=["Invalid credentials"],
                    error_code="authentication_failed",
                    status_code=status.HTTP_401_UNAUTHORIZED,
                )

            if not user.is_active:
                return ErrorResponse(
                    message="Account is inactive",
                    errors=["Your account has been disabled."],
                    error_code="account_inactive",
                    status_code=status.HTTP_403_FORBIDDEN,
                )
            response_serializer = LoginResponseSerializer(user)
            return SuccessResponse(
                message="Login Successful!", data=response_serializer.data
            )

        # Handle serializer validation errors
        formatted_errors = format_serializer_errors(serializer.errors)
        return ErrorResponse(
            message="Login failed",
            errors=formatted_errors,
            error_code="login_error",
            status_code=status.HTTP_400_BAD_REQUEST,
        )


class RegisterUserView(GenericAPIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_serializer = LoginResponseSerializer(user)
            return SuccessResponse(
                message="Registration Successful!", data=response_serializer.data
            )

        # Handle serializer validation errors
        formatted_errors = format_serializer_errors(serializer.errors)
        return ErrorResponse(
            message="Registration failed",
            errors=formatted_errors,
            error_code="reg_error",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
