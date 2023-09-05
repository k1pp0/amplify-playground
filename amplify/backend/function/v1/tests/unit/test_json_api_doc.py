import pytest


from src.common.json_api_doc import JsonApiDoc

class DummyModel:
    dummy_model_id = 'dummy_model_id'
    field1 = 'field1'
    field2 = 'field2'
    
@pytest.fixture
def fixture_json_api_doc():
    return JsonApiDoc(DummyModel)


def test_json_api_to_model_class_dict(fixture_json_api_doc):
    json_api_dict = {
        "data": {
            "type": "dummy_model",
            "id": "1",
            "attributes": {
                "field1": "field1 string",
                "field2": 2
            }
        }
    }

    expected_dict = {
        "dummy_model_id": "1",
        "field1": "field1 string",
        "field2": 2
    }

    assert fixture_json_api_doc.json_api_to_model_class_dict(json_api_dict) == expected_dict

def test_model_class_to_json_api_dict(fixture_json_api_doc):
    model_class_dict = {
        "dummy_model_id": "1",
        "field1": "field1 string",
        "field2": 2
    }

    expected_dict = {
        "data": {
            "type": "dummy_model",
            "id": "1",
            "attributes": {
                "field1": "field1 string",
                "field2": 2
            }
        }
    }

    assert fixture_json_api_doc.model_class_to_json_api_dict(model_class_dict) == expected_dict

def test_json_api_to_model_class_dict_with_empty_dict(fixture_json_api_doc):
    json_api_dict = {}
    with pytest.raises(ValueError):
        fixture_json_api_doc.json_api_to_model_class_dict(json_api_dict)

def test_json_api_to_model_class_dict_with_not_exists_fields(fixture_json_api_doc):
    json_api_dict = {
        "data": {
            "type": "dummy_model",
            "id": "1",
            "attributes": {
                "field1": "field1 string",
                "field2": 2,
                "not_exists_field": "not_exists_field"
            }
        }
    }
    with pytest.raises(ValueError):
        fixture_json_api_doc.json_api_to_model_class_dict(json_api_dict)

def test_model_class_to_json_api_dict_with_not_exists_fields(fixture_json_api_doc):
    model_class_dict = {
        "dummy_model_id": "1",
        "field1": "field1 string",
        "field2": 2,
        "not_exists_field": "not_exists_field"
    }
    with pytest.raises(ValueError):
        fixture_json_api_doc.model_class_to_json_api_dict(model_class_dict)