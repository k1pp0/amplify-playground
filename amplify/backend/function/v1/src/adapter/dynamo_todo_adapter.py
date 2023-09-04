import boto3
import os
from functools import reduce
from typing import List

from boto3.dynamodb.conditions import Key, Attr

from model.todo import Todo
from interface.adapter.i_todo_adapter import ITodoAdapter


class DynamoTodoAdapter(ITodoAdapter):
    
    def __init__(self, table_name: str):
        self._dynamodb = boto3.resource('dynamodb', endpoint_url=os.environ.get('DYNAMO_ENDPOINT_URL', None))
        self._table = self._dynamodb.Table(f"{table_name}-{os.environ.get('ENVIRONMENT', None)}")
    
    def read(self, todo_id: str, params: dict) -> Todo:
        query_parameters = {}
        query_parameters["Key"] = {'todo_id': todo_id}
        if len(params['fields']) != 0:
            query_parameters["ProjectionExpression"] = self.build_projection_expression(params['fields'])
        response = self._table.get_item(**query_parameters)
        item = response.get('Item')
        if item:
            return Todo(**item)
        else:
            raise ValueError(f"Todo with ID {todo_id} not found.")
    
    def list(self, params: dict) -> List[Todo]:
        query_parameters = {}
        if len(params['fields']) != 0:
            query_parameters["ProjectionExpression"] = self.build_projection_expression(params['fields'])
        if len(params['filters']) != 0:
            query_parameters["FilterExpression"] = self.build_filter_expression(params['filters'])
        response = self._table.scan(**query_parameters)
        todos = [Todo(**item) for item in response.get('Items', [])]
        return todos
    
    def create(self, todo: Todo) -> Todo:
        response = self._table.put_item(Item=todo.to_dict())
        return todo

    def build_filter_expression(self, filters: List[dict]) -> boto3.dynamodb.conditions:
        if len(filters) == 0:
            return None

        operator_map = {
            "eq": lambda k, v: Attr(k).eq(v),
            "ne": lambda k, v: Attr(k).ne(v),
            "lt": lambda k, v: Attr(k).lt(v),
            "le": lambda k, v: Attr(k).lte(v),
            "gt": lambda k, v: Attr(k).gt(v),
            "ge": lambda k, v: Attr(k).gte(v),
            "begins_with": lambda k, v: Attr(k).begins_with(v),
            "contains": lambda k, v: Attr(k).contains(v),
            "in": lambda k, v: Attr(k).is_in(v if isinstance(v, list) else [v]),
            "between": lambda k, v: ~Attr(k).eq(v),
            "not": lambda k, v: Attr(k).between(v[0], v[1]),
            "attribute_exists": lambda k, _: Attr(k).exists(),
            "attribute_not_exists": lambda k, _: Attr(k).not_exists()
        }

        filter_expressions = [
            operator_map[filter_item["operator"]](filter_item["key"], filter_item["value"])
            for filter_item in filters
            if filter_item["operator"] in operator_map
        ]
        filter_expression = reduce(lambda x, y: x & y, filter_expressions)
        return filter_expression
    
    def build_projection_expression(self, fields: List[str]) -> str:
        if len(fields) == 0:
            return None
        
        projection_expression = ", ".join(fields)
        return projection_expression
