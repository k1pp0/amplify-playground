import pytest
from src.common.query_string_parameters import QueryStringParameters

class DummyModel:
    dummy_model_id = 'dummy_model_id'
    field1 = 'field1'
    field2 = 'field2'

@pytest.fixture
def fixture_query_string_parameters():
    return QueryStringParameters(DummyModel)

def test_convert_with_empty_params(fixture_query_string_parameters):
    params: dict = {}
    result: dict = fixture_query_string_parameters.convert(params)
    assert result == {"fields": [], "filters": [], "sort": [], "page_offset": 0, "page_size": 10}

def test_convert_with_none_params(fixture_query_string_parameters):
    params: dict = None
    result: dict = fixture_query_string_parameters.convert(params)
    assert result == {"fields": [], "filters": [], "sort": [], "page_offset": 0, "page_size": 10}

def test_convert_with_valid_fields(fixture_query_string_parameters):
    params: dict = {"fields[dummy_model]": "field1,field2"}
    result: dict = fixture_query_string_parameters.convert(params)
    assert set(result["fields"]) == {"field1", "field2", "dummy_model_id"}

def test_convert_with_invalid_fields(fixture_query_string_parameters):
    params: dict = {"fields[dummy_model]": "field1,field3"}
    with pytest.raises(ValueError):
        fixture_query_string_parameters.convert(params)

def test_convert_with_valid_filters(fixture_query_string_parameters):
    params: dict = {"filter[field1][eq]": "value1"}
    result: dict = fixture_query_string_parameters.convert(params)
    assert result["filters"] == [{"key": "field1", "operator": "eq", "value": "value1"}]

def test_convert_with_invalid_filters(fixture_query_string_parameters):
    params: dict = {"filter[field3][eq]": "value1"}
    with pytest.raises(ValueError):
        fixture_query_string_parameters.convert(params)

def test_convert_with_invalid_operator(fixture_query_string_parameters):
    params: dict = {"filter[field1][invalid]": "value1"}
    with pytest.raises(ValueError):
        fixture_query_string_parameters.convert(params)

def test_convert_with_valid_sort(fixture_query_string_parameters):
    params: dict = {"sort": "field1,-field2"}
    result: dict = fixture_query_string_parameters.convert(params)
    assert result["sort"] == [{"key": "field1", "order": "asc"}, {"key": "field2", "order": "desc"}]

def test_convert_with_invalid_sort(fixture_query_string_parameters):
    params: dict = {"sort": "field1,-field3"}
    with pytest.raises(ValueError):
        fixture_query_string_parameters.convert(params)

def test_convert_with_invalid_page_offset(fixture_query_string_parameters):
    params: dict = {"page[offset]": "invalid"}
    with pytest.raises(ValueError):
        fixture_query_string_parameters.convert(params)

def test_convert_with_invalid_page_size(fixture_query_string_parameters):
    params: dict = {"page[size]": "invalid"}
    with pytest.raises(ValueError):
        fixture_query_string_parameters.convert(params)
