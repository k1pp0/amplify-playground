import os

from common.service_result import ServiceResult

from service.todo_service import TodoService
from port.todo_port import TodoPort
from adapter.dynamo_todo_adapter import DynamoTodoAdapter


def main():
    todo_service: TodoService = TodoService(TodoPort(DynamoTodoAdapter(table_name="Todos")))

    result: ServiceResult = todo_service.read_todo('id_1')
    print(result)

    result: ServiceResult = todo_service.read_todo('id_11')
    print(result)

    query_string_parameters: dict = {
        # "fields[todo]": "title,description,due_date", 
        # "page[offset]": "0",
        # "page[size]": "10", 
        # "filter[due_date][le]": "2023-08-14", 
        # "sort": "description,-due_date"
    }
    result: ServiceResult = todo_service.list_todo(query_string_parameters)
    print(result)

if __name__ == "__main__":
    main()