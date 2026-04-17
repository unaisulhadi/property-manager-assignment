def format_serializer_errors(errors):
    """
    Utility function to format serializer errors into a meaningful message.

    Args:
        errors (dict or any): The errors object from a serializer.

    Returns:
        str: A formatted error message or raw string if the format is unexpected.
    """
    error_messages = []

    try:
        # Check if errors is a dictionary-like structure
        if isinstance(errors, dict):
            for field, field_errors in errors.items():
                for error in field_errors:
                    error_messages.append(f"{field}: {error}")
        else:
            # If errors is not a dict, use its raw string representation
            return str(errors)

        # Join the messages into a single string
        return " | ".join(error_messages) if error_messages else str(errors)

    except Exception as e:
        # In case of any unexpected error, fallback to the raw string representation
        return f"Error processing: {str(errors)}. Exception: {str(e)}"
