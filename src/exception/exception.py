import traceback
import src.constants.error_messages as error_messages
import src.logging.logging as logging

class ProjectException(Exception):
    """
    Custom Exception class for production environment with:
    - Standardized error messages and error codes
    - Automatic logging with stack trace
    """

    def __init__(self, error_code="ERR_999", message=None, details=None):
        """
        :param error_code: Standardized error code (default: "ERR_999" for unknown errors)
        :param message: Optional custom error message (if None, uses predefined message)
        :param details: Optional additional details (e.g., user_id, filename)
        """
        self.error_code = error_code
        self.message = message or error_messages.ERROR.get(error_code, "Unexpected error occurred")
        self.details = details
        self.full_message = f"[{self.error_code}] {self.message}"

        if self.details:
            self.full_message += f" | Details: {self.details}"

        # Call base class constructor with the full message
        super().__init__(self.full_message)

        # Capture full stack trace
        error_traceback = traceback.format_exc() or "No stack trace available"

    def __str__(self):
        return f"{self.__class__.__name__}: {self.full_message}"