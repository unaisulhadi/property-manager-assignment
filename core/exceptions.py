import logging

from django.db.utils import IntegrityError
from rest_framework.views import exception_handler
from rest_framework_simplejwt.exceptions import (
    InvalidToken,
    TokenError,
    AuthenticationFailed as JWTAuthenticationFailed,
)
from rest_framework.exceptions import (
    APIException,
    AuthenticationFailed,
    NotAuthenticated,
    PermissionDenied,
    NotFound,
    MethodNotAllowed,
    NotAcceptable,
    UnsupportedMediaType,
    ParseError,
    Throttled,
)

from core.response import ErrorResponse

logger = logging.getLogger("base_logger")


class CustomExceptionHandler:
    """
    Custom Exception Handler for handling all exceptions from Django REST framework and JWT.
    """

    status_code_mapping = {
        NotFound: 404,
        PermissionDenied: 403,
        AuthenticationFailed: 401,
        NotAuthenticated: 401,
        JWTAuthenticationFailed: 401,
        InvalidToken: 401,
        TokenError: 401,
        MethodNotAllowed: 405,
        NotAcceptable: 406,
        UnsupportedMediaType: 415,
        ParseError: 400,
        IntegrityError: 400,
        APIException: 500,
        Throttled: 429,  # Special case for rate-limiting or throttling errors
    }

    exception_messages = {
        AuthenticationFailed: "Authentication failed. Please provide valid credentials.",
        JWTAuthenticationFailed: "JWT Authentication failed. Invalid token or credentials.",
        NotAuthenticated: "You are not authenticated. Please log in to access this resource.",
        PermissionDenied: "You do not have permission to perform this action.",
        NotFound: "The requested resource was not found.",
        MethodNotAllowed: "The HTTP method used is not allowed for this endpoint.",
        NotAcceptable: "The request format is not acceptable. Please modify your request.",
        UnsupportedMediaType: "The media type of the request is unsupported. Please use a supported format.",
        ParseError: "The request could not be parsed due to invalid syntax.",
        IntegrityError: "A database integrity error occurred, likely due to duplicate or invalid data.",
        InvalidToken: "The provided token is invalid or has expired. Please obtain a new token.",
        TokenError: "Token-related error. The token is invalid, expired, or malformed.",
        Throttled: "Too many requests. Please try again later.",
        APIException: "An internal server error occurred. Please try again later.",
    }

    @classmethod
    def get_error_message(cls, exc):
        """
        Returns a meaningful error message based on the exception type.
        """
        # Get a custom message for the exception type, or use the exception string if not specified
        if type(exc) in cls.exception_messages:
            return cls.exception_messages[type(exc)]

        # For any other exceptions, return the default message
        return str(exc) if exc else "An unexpected error occurred."

    def __new__(cls, exc, context):
        # Log the exception details with appropriate severity level
        logger.error(f"Exception occurred: {exc}")

        # Default response from DRF's exception handler
        _ = exception_handler(exc, context)

        # Determine the status code based on exception type
        status_code = cls.status_code_mapping.get(type(exc), 500)

        # Generate a meaningful error message based on exception type
        message = cls.get_error_message(exc)

        # Return the custom ErrorResponse with status code and message
        return ErrorResponse(status_code=status_code, message=message)
