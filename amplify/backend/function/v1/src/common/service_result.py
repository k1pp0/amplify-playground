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
