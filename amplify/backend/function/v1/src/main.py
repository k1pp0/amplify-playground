from common.service_result import ServiceResult

from service.todo_service import TodoService
from port.todo_port import TodoPort
from adapter.local_todo_adapter import LocalTodoAdapter


def main():
    todo_service: TodoService = TodoService(TodoPort(LocalTodoAdapter()))

    result: ServiceResult = todo_service.read_todo('id_1')
    print(result)

    result: ServiceResult = todo_service.read_todo('id_11')
    print(result)

if __name__ == "__main__":
    main()