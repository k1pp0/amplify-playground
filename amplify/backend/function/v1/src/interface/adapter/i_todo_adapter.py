from abc import ABCMeta, abstractmethod

from model.todo import Todo


class ITodoAdapter(metaclass=ABCMeta):
    
    @abstractmethod
    def read(self, todo_id: str) -> Todo:
        raise NotImplementedError()
