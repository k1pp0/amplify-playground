import pytest

from src.model.todo import Todo

@pytest.fixture()
def fixture_todo_0() -> Todo:
    return Todo(
        todo_id="id_0",
        title="Task 0",
        description="Description for Task 0",
        due_date="2023-08-10",
        is_completed=False
    )

def test_todo_is_completed(fixture_todo_0):
    target: Todo = fixture_todo_0
    
    assert target.is_completed == False
    target.mark_as_completed()
    assert target.is_completed == True
    target.mark_as_incomplete()
    assert target.is_completed == False
