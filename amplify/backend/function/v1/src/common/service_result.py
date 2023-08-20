from http import HTTPStatus


class ServiceResult:
    def __init__(self, status: HTTPStatus, json: dict):
        self.__status = status
        self.__json = json

    @property
    def status(self):
        return self.__status
    
    @property
    def json(self):
        return self.__json

    def __str__(self):
        return f"status: {self.__status}, json: {self.json}"
