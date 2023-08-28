import pytest
from typing import List

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

def test_todo_to_dict_without_fields(fixture_todo_0):
    target: Todo = fixture_todo_0

    target_dict: dict = target.to_dict()
    assert ("todo_id" in target_dict) == True
    assert ("title" in target_dict) == True
    assert ("description" in target_dict) == True
    assert ("due_date" in target_dict) == True
    assert ("is_completed" in target_dict) == True

def test_todo_to_dict_with_fields(fixture_todo_0):
    target: Todo = fixture_todo_0
    fields: List[str] = ["todo_id", "title"]

    target_dict: dict = target.to_dict(fields)
    assert ("todo_id" in target_dict) == True
    assert ("title" in target_dict) == True
    assert ("is_completed" in target_dict) == False
