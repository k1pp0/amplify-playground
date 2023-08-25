from http import HTTPStatus
import json

from interface.port.i_todo_port import ITodoPort
from common.service_result import ServiceResult
from model.todo import Todo

class TodoService():
    def __init__(self, todo_port: ITodoPort):
        self.__todo_port = todo_port

    def read_todo(self, todo_id: str) -> ServiceResult:
        try:
            todo = self.__todo_port.read_todo(todo_id)
            return ServiceResult(status=HTTPStatus.OK, json=todo.to_json())
        except ValueError:
            return ServiceResult(status=HTTPStatus.NOT_FOUND, json=None)

    def list_todo(self, query_string_parameters: dict) -> ServiceResult:

        def todo_default(o):
            if isinstance(o, Todo):
                return o.to_json()
            raise TypeError(repr(o) + " is not JSON serializable")
        
        try:
            todos = self.__todo_port.list_todo(query_string_parameters)
            return ServiceResult(status=HTTPStatus.OK, json=json.dumps(todos, default=todo_default))
        except ValueError:
            return ServiceResult(status=HTTPStatus.NOT_FOUND, json=None)
        