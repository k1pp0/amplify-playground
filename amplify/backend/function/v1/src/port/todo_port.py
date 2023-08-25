from typing import List

from model.todo import Todo
from interface.port.i_todo_port import ITodoPort
from interface.adapter.i_todo_adapter import ITodoAdapter
from common.query_string_parameters import QueryStringParameters


class TodoPort(ITodoPort):
    def __init__(self, adapter: ITodoAdapter):
        self.__adapter = adapter

    def read_todo(self, todo_id: str) -> Todo:
        todo = self.__adapter.read(todo_id)
        return todo

    def list_todo(self, query_string_parameters: dict) -> List[Todo]:
        converter: QueryStringParameters = QueryStringParameters(Todo)
        params: dict = converter.convert(query_string_parameters)
        todos: List[Todo] = self.__adapter.list(params)
        return todos