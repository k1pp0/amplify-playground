from http import HTTPStatus

from interface.port.i_todo_port import ITodoPort
from common.service_result import ServiceResult


class TodoService():
    def __init__(self, todo_port: ITodoPort):
        self.__todo_port = todo_port

    def read_todo(self, todo_id: str) -> ServiceResult:
        try:
            todo = self.__todo_port.read_todo(todo_id)
            return ServiceResult(status=HTTPStatus.OK, json=todo.to_json())
        except ValueError:
            return ServiceResult(status=HTTPStatus.NOT_FOUND, json=None)