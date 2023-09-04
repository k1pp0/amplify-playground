import pytest
from src.common.query_string_parameters import QueryStringParameters

class DummyModel:
    dummy_model_id = 'dummy_model_id'
    field1 = 'field1'
    field2 = 'field2'

@pytest.fixture
def query_obj():
    return QueryStringParameters(DummyModel)

def test_convert_with_empty_params(query_obj):
    params = {}
    result = query_obj.convert(params)
    assert result == {"fields": [], "filters": [], "sort": [], "page_offset": 0, "page_size": 10}

def test_convert_with_none_params(query_obj):
    params = None
    result = query_obj.convert(params)
    assert result == {"fields": [], "filters": [], "sort": [], "page_offset": 0, "page_size": 10}

def test_convert_with_valid_fields(query_obj):
    params = {"fields[dummy_model]": "field1,field2"}
    result = query_obj.convert(params)
    assert set(result["fields"]) == {"field1", "field2", "dummy_model_id"}

def test_convert_with_invalid_fields(query_obj):
    params = {"fields[dummy_model]": "field1,field3"}
    with pytest.raises(ValueError):
        query_obj.convert(params)

def test_convert_with_valid_filters(query_obj):
    params = {"filter[field1][eq]": "value1"}
    result = query_obj.convert(params)
    assert result["filters"] == [{"key": "field1", "operator": "eq", "value": "value1"}]

def test_convert_with_invalid_filters(query_obj):
    params = {"filter[field3][eq]": "value1"}
    with pytest.raises(ValueError):
        query_obj.convert(params)

def test_convert_with_invalid_operator(query_obj):
    params = {"filter[field1][invalid]": "value1"}
    with pytest.raises(ValueError):
        query_obj.convert(params)

def test_convert_with_valid_sort(query_obj):
    params = {"sort": "field1,-field2"}
    result = query_obj.convert(params)
    assert result["sort"] == [{"key": "field1", "order": "asc"}, {"key": "field2", "order": "desc"}]

def test_convert_with_invalid_sort(query_obj):
    params = {"sort": "field1,-field3"}
    with pytest.raises(ValueError):
        query_obj.convert(params)

def test_convert_with_invalid_page_offset(query_obj):
    params = {"page[offset]": "invalid"}
    with pytest.raises(ValueError):
        query_obj.convert(params)

def test_convert_with_invalid_page_size(query_obj):
    params = {"page[size]": "invalid"}
    with pytest.raises(ValueError):
        query_obj.convert(params)
