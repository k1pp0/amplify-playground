from http import HTTPStatus
import json

from interface.port.i_todo_port import ITodoPort
from common.service_result import ServiceResult
from model.todo import Todo

class TodoService():
    def __init__(self, todo_port: ITodoPort):
        self._todo_port = todo_port

    def read_todo(self, todo_id: str) -> ServiceResult:
        try:
            todo = self._todo_port.get_todo_by_id(todo_id)
            return ServiceResult(status=HTTPStatus.OK, body=json.dumps(todo.to_dict()))
        except ValueError:
            return ServiceResult(status=HTTPStatus.NOT_FOUND, body=None)

    def list_todo(self, query_string_parameters: dict) -> ServiceResult:

        def todo_default(o):
            if isinstance(o, Todo):
                return o.to_dict()
            raise TypeError(repr(o) + " is not JSON serializable")
        
        try:
            todos = self._todo_port.list_todo_with_query_string_parameters(query_string_parameters)
            return ServiceResult(status=HTTPStatus.OK, body=json.dumps(todos, default=todo_default))
        except ValueError:
            return ServiceResult(status=HTTPStatus.NOT_FOUND, body=None)
        