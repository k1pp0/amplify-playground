from http import HTTPStatus


class ServiceResult:
    def __init__(self, status: HTTPStatus, body: dict):
        self._status = status
        self._body = body

    @property
    def status(self):
        return self._status
    
    @property
    def body(self):
        return self._body

    def __str__(self):
        return f"status: {self._status}, body: {self._body}"
