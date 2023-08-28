import os
import boto3

from common.service_result import ServiceResult

from model.todo import Todo
from service.todo_service import TodoService
from port.todo_port import TodoPort
from adapter.dynamo_todo_adapter import DynamoTodoAdapter


def main():
    todo_service: TodoService = TodoService(TodoPort(DynamoTodoAdapter(table_name="Todos")))

    query_string_parameters: dict = {
        "fields[todo]": "title", 
    }
    result: ServiceResult = todo_service.read_todo('id_1', query_string_parameters)
    print(result)

    result: ServiceResult = todo_service.read_todo('id_1', None)
    print(result)

    result: ServiceResult = todo_service.read_todo('id_11', query_string_parameters)
    print(result)

    query_string_parameters: dict = {
        "fields[todo]": "title,description,is_completed,due_date", 
        "page[offset]": "0",
        "page[size]": "10", 
        "filter[due_date][le]": "2020-01-15", 
        "filter[description][contains]": "Odd", 
        "sort": "description,-due_date"
    }
    result: ServiceResult = todo_service.list_todo(query_string_parameters)
    print(result)

    result: ServiceResult = todo_service.list_todo(None)
    print(result)


def setup():
    dynamodb = boto3.resource('dynamodb', endpoint_url=os.environ.get('DYNAMO_ENDPOINT_URL', None))
    table = dynamodb.Table(f"Todos-{os.environ.get('ENVIRONMENT', None)}")
    
    todo_data = []
    for i in range(10):
        todo_data.append(Todo(
            todo_id=f"id_{i}",
            title=f"Task {i}",
            description=f"Description for Task { 'Odd' if i % 2 == 1 else 'Even' }",
            due_date=f"2020-01-{20-i}",
            is_completed=True if i % 5 == 0 else False
        ))

    for todo in todo_data:
        table.put_item(Item=todo.to_dict())


if __name__ == "__main__":
    setup()
    main()