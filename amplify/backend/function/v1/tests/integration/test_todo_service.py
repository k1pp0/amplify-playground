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


class DummyTodoAdapter(ITodoAdapter):
    def read(self, todo_id: str) -> Todo:
        if todo_id == test_todo_0.todo_id:
            return test_todo_0
        else:
            raise ValueError(f"Todo with ID {todo_id} not found.")

@pytest.fixture()
def fixture_todo_service():
    todo_service: TodoService = TodoService(TodoPort(DummyTodoAdapter()))
    yield todo_service
    todo_service = None

def test_todo_service_exist(fixture_todo_service):
    target: TodoService = fixture_todo_service
    result: ServiceResult = target.read_todo(test_todo_0.todo_id)
    todo: dict = json.loads(result.json)

    assert result != None
    assert result.status.value == 200
    assert todo["todo_id"] == test_todo_0.todo_id
    assert todo["title"] == test_todo_0.title
    assert todo["description"] == test_todo_0.description
    assert todo["due_date"] == test_todo_0.due_date
    assert todo["is_completed"] == test_todo_0.is_completed

def test_todo_service_not_exist(fixture_todo_service):
    target: TodoService = fixture_todo_service
    result: ServiceResult = target.read_todo("not_exist_id")

    assert result != None
    assert result.status.value == 404
    assert result.json == None
