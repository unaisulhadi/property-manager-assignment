from rest_framework.response import Response


class SuccessResponse(Response):
    status_code = 200

    def __init__(self, message=None, data=None, status_code=200):

        data_content = {
            'success': True,
            'status_code': status_code,
            'message': message,
            'data': data,
        }
        super().__init__(data=data_content, status=status_code)


class ErrorResponse(Response):

    def __init__(self, message=None, errors=None,
                 error_code=None, status_code=400):
        self.status_code = status_code
        data_content = {
            'success': False,
            'error_code': error_code,
            'message': message,
            'errors': errors,
        }
        super().__init__(data=data_content, status=status_code)
