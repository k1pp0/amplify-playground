from abc import ABCMeta, abstractmethod
from typing import List

from model.todo import Todo


class ITodoPort(metaclass=ABCMeta):

    @abstractmethod
    def get_todo_by_id(self, todo_id:str, query_string_parameters: dict) -> Todo:
        raise NotImplementedError()

    @abstractmethod
    def list_todo_with_query_string_parameters(self, query_string_parameters: dict) -> List[Todo]:
        raise NotImplementedError()
