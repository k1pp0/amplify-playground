import json
from http import HTTPStatus

from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.event_handler import (
    APIGatewayRestResolver,
    Response,
    content_types,
)
from aws_lambda_powertools import Logger
from aws_lambda_powertools.logging import correlation_paths

from common.service_result import ServiceResult

from service.todo_service import TodoService
from port.todo_port import TodoPort
from adapter.local_todo_adapter import LocalTodoAdapter

app = APIGatewayRestResolver()
logger = Logger(service='playground', use_rfc3339=True) 

@app.get("/api/v1/hello")
def hello() -> dict:
    result: dict = ServiceResult(
        status=HTTPStatus.OK,
        json=json.dumps('Hello from your new Amplify Python lambda!')
    )
    response: Response = Response(
        status_code=result.status.value,
        content_type=content_types.APPLICATION_JSON,
        body=result.json
    )
    return response

@app.get("/api/v1/todos/<todo_id>")
def read_todo(todo_id: str) -> dict:
    todo_service: TodoService = TodoService(TodoPort(LocalTodoAdapter()))
    result: ServiceResult = todo_service.read_todo(todo_id)
    logger.info(result)
    response: Response = Response(
        status_code=result.status.value,
        content_type=content_types.APPLICATION_JSON,
        body=result.json
    )
    return response

@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
def handler(event, context):
    logger.info(event)
    response: dict = app.resolve(event, context)
    response['headers'] = {
        'Access-Control-Allow-Headers': '*',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    }
    logger.info(response)
    return response
