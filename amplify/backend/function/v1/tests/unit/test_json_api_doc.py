import pytest

from src.model.todo import Todo
from src.common.json_api_doc import JsonApiDoc

json_api_doc = JsonApiDoc(model=Todo)

def test_generate_model_name():
    assert json_api_doc._generate_model_name(Todo) == "todo"

def test_extract_model_fields():
    expected_fields = ['description', 'due_date', 'is_completed', 'todo_id', 'title']
    assert sorted(json_api_doc._model_fields) == sorted(expected_fields)

def test_validate_model_field_valid():
    try:
        json_api_doc._validate_model_field('title')
    except ValueError:
        pytest.fail("Unexpected ValueError ..")

def test_validate_model_field_invalid():
    with pytest.raises(ValueError):
        json_api_doc._validate_model_field('invalid_field')

def test_json_api_to_model_class_dict():
    json_api_data = {
        "data": {
            "id": "1",
            "attributes": {
                "title": "Test Todo",
                "description": "This is a test",
                "due_date": "2023-12-31",
                "is_completed": False
            }
        }
    }

    expected_dict = {
        "todo_id": "1",
        "title": "Test Todo",
        "description": "This is a test",
        "due_date": "2023-12-31",
        "is_completed": False
    }

    assert json_api_doc.json_api_to_model_class_dict(json_api_data) == expected_dict

def test_model_class_to_json_api_dict():
    model_class_dict = {
        "todo_id": "1",
        "title": "Test Todo",
        "description": "This is a test",
        "due_date": "2023-12-31",
        "is_completed": False
    }

    expected_json_api_dict = {
        "data": {
            "type": "todo",
            "id": "1",
            "attributes": {
                "title": "Test Todo",
                "description": "This is a test",
                "due_date": "2023-12-31",
                "is_completed": False
            }
        }
    }

    assert json_api_doc.model_class_to_json_api_dict(model_class_dict) == expected_json_api_dict