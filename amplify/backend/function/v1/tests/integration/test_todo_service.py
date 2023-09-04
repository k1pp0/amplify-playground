import pytest
import sys
import json

sys.path.append('/workspace/amplify/backend/function/v1/src/')
from src.model.todo import Todo
from src.common.service_result import ServiceResult
from src.service.todo_service import TodoService
from src.port.todo_port import TodoPort
from src.interface.adapter.i_todo_adapter import ITodoAdapter

test_todo_0: Todo = Todo(
    todo_id="id_0",
    title="Task 0",
    description="Description for Task 0",
    due_date="2023-08-10",
    is_completed=False
)

test_todo_1: Todo = Todo(
    todo_id="id_1",
    title="Task 1",
    description="Description for Task 1",
    due_date="2023-08-11",
    is_completed=True
)


class DummyTodoAdapter(ITodoAdapter):
    def read(self, todo_id: str, params: dict) -> Todo:
        if todo_id == test_todo_0.todo_id:
            return test_todo_0
        else:
            raise ValueError(f"Todo with ID {todo_id} not found.")
        
    def list(self, params: dict) -> Todo:
        return [test_todo_0, test_todo_1]

    def create(self, params: dict) -> Todo:
        return test_todo_0

@pytest.fixture()
def fixture_todo_service():
    todo_service: TodoService = TodoService(TodoPort(DummyTodoAdapter()))
    yield todo_service
    todo_service = None

def test_todo_service_read_todo_with_exist_id(fixture_todo_service):
    target: TodoService = fixture_todo_service
    result: ServiceResult = target.read_todo(test_todo_0.todo_id, None)
    todo: dict = json.loads(result.body)

    assert result != None
    assert result.status.value == 200
    assert todo["data"]["id"] == test_todo_0.todo_id
    assert todo["data"]["attributes"]["title"] == test_todo_0.title
    assert todo["data"]["attributes"]["description"] == test_todo_0.description
    assert todo["data"]["attributes"]["due_date"] == test_todo_0.due_date
    assert todo["data"]["attributes"]["is_completed"] == test_todo_0.is_completed

def test_todo_service_read_todo_with_not_exist_id(fixture_todo_service):
    target: TodoService = fixture_todo_service
    result: ServiceResult = target.read_todo("not_exist_id", {})

    assert result != None
    assert result.status.value == 404
    assert result.body == None

def test_todo_service_list_todo(fixture_todo_service):
    target: TodoService = fixture_todo_service
    result: ServiceResult = target.list_todo(None)
    todos: dict = json.loads(result.body)

    assert result != None
    assert result.status.value == 200
    assert len(todos) == 2
    assert todos[1]["data"]["id"] == test_todo_1.todo_id
    assert todos[1]["data"]["attributes"]["title"] == test_todo_1.title
    assert todos[1]["data"]["attributes"]["description"] == test_todo_1.description
    assert todos[1]["data"]["attributes"]["due_date"] == test_todo_1.due_date
    assert todos[1]["data"]["attributes"]["is_completed"] == test_todo_1.is_completed
