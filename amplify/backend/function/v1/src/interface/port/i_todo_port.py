from abc import ABCMeta, abstractmethod

from model.todo import Todo


class ITodoPort(metaclass=ABCMeta):

    @abstractmethod
    def read_todo(self, todo_id:str) -> Todo:
        raise NotImplementedError()
