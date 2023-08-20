from model.todo import Todo
from interface.port.i_todo_port import ITodoPort
from interface.adapter.i_todo_adapter import ITodoAdapter


class TodoPort(ITodoPort):
    def __init__(self, adapter: ITodoAdapter):
        self.__adapter = adapter

    def read_todo(self, todo_id: str) -> Todo:
        todo = self.__adapter.read(todo_id)
        return todo