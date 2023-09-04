from typing import List

from model.todo import Todo
from interface.port.i_todo_port import ITodoPort
from interface.adapter.i_todo_adapter import ITodoAdapter
from common.query_string_parameters import QueryStringParameters
from common.json_api_doc import JsonApiDoc


class TodoPort(ITodoPort):
    def __init__(self, adapter: ITodoAdapter):
        self._adapter = adapter
        self._converter = QueryStringParameters(Todo)
        self._serialize = JsonApiDoc(Todo)

    def get_todo_by_id(self, todo_id: str, query_string_parameters: dict) -> Todo:
        params: dict = self._converter.convert(query_string_parameters)
        fields: List[str] = params.get('fields', None)
        todo: Todo = self._adapter.read(todo_id, params)
        return self._serialize.model_class_to_json_api_dict(todo.to_dict(fields))

    def list_todo_with_query_string_parameters(self, query_string_parameters: dict) -> List[Todo]:
        params: dict = self._converter.convert(query_string_parameters)
        fields: List[str] = params.get('fields', None)
        todos: List[Todo] = [self._serialize.model_class_to_json_api_dict(todo.to_dict(fields)) for todo in self._adapter.list(params)]
        return todos
    
    def create_todo(self, request_body: dict) -> Todo:
        model_class_dict = self._serialize.json_api_to_model_class_dict(request_body)
        request_todo: Todo = Todo(**model_class_dict)
        request_todo.set_new_uuid()
        todo: Todo = self._adapter.create(request_todo)
        return todo.to_dict()