import boto3
import os
from typing import List

from model.todo import Todo
from interface.adapter.i_todo_adapter import ITodoAdapter


class DynamoTodoAdapter(ITodoAdapter):
    
    def __init__(self, table_name: str):
        self._dynamodb = boto3.resource('dynamodb', endpoint_url=os.environ.get('DYNAMO_ENDPOINT_URL', None))
        self._table = self._dynamodb.Table(f"{table_name}-{os.environ.get('ENVIRONMENT', None)}")
    
    def read(self, todo_id: str) -> Todo:
        response = self._table.get_item(Key={'todo_id': todo_id})
        item = response.get('Item')
        if item:
            return Todo(
                todo_id=item['todo_id'],
                title=item['title'],
                description=item['description'],
                due_date=item['due_date']
            )
        else:
            raise ValueError(f"Todo with ID {todo_id} not found.")
    
    def list(self, params: dict) -> List[Todo]:
        return None
