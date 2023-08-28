from abc import ABCMeta, abstractmethod
from typing import List

from model.todo import Todo


class ITodoAdapter(metaclass=ABCMeta):
    
    @abstractmethod
    def read(self, todo_id: str, params: dict) -> Todo:
        raise NotImplementedError()

    @abstractmethod
    def list(self, params: dict) -> List[Todo]:
        raise NotImplementedError()
