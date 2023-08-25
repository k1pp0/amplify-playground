from abc import ABCMeta, abstractmethod
from typing import List

from model.todo import Todo


class ITodoPort(metaclass=ABCMeta):

    @abstractmethod
    def read_todo(self, todo_id:str) -> Todo:
        raise NotImplementedError()

    @abstractmethod
    def list_todo(self, query_string_parameters: dict) -> List[Todo]:
        raise NotImplementedError()
