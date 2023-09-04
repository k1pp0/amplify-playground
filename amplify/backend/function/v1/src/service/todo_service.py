from http import HTTPStatus
import json

from interface.port.i_todo_port import ITodoPort
from common.service_result import ServiceResult

class TodoService():
    def __init__(self, todo_port: ITodoPort):
        self._todo_port = todo_port

    def read_todo(self, todo_id: str, query_string_parameters: dict) -> ServiceResult:
        try:
            todo = self._todo_port.get_todo_by_id(todo_id, query_string_parameters)
            return ServiceResult(status=HTTPStatus.OK, body=json.dumps(todo))
        except ValueError:
            return ServiceResult(status=HTTPStatus.NOT_FOUND, body=None)
        # except ValueError as value_error:
            # error_body: dict = {
            #     "status": HTTPStatus.BAD_REQUEST.value,
            #     "title": "Invalid Attribute",
            #     "detail": value_error
            # }
            # return ServiceResult(status=HTTPStatus.NOT_FOUND, body=error_body)

    def list_todo(self, query_string_parameters: dict) -> ServiceResult:
        try:
            todos = self._todo_port.list_todo_with_query_string_parameters(query_string_parameters)
            return ServiceResult(status=HTTPStatus.OK, body=json.dumps(todos))
        except ValueError:
            return ServiceResult(status=HTTPStatus.NOT_FOUND, body=None)
        
    def create_todo(self, request_body: dict) -> ServiceResult:
        try:
            todo = self._todo_port.create_todo(request_body)
            return ServiceResult(status=HTTPStatus.OK, body=json.dumps(todo))
        except ValueError:
            return ServiceResult(status=HTTPStatus.NOT_FOUND, body=None)
