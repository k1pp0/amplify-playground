import re
from typing import Any, List

class QueryStringParameters:

    ALLOWED_OPERATORS = set([
        "eq", "ne", "lt", "le", "gt", "ge",
        "startswith", "contains",
        "in", "between", "not",
        "attribute_exists", "attribute_not_exists"
    ])

    def __init__(self, model: Any):
        self._model_name = self._generate_model_name(model)
        self._model_fields = self._extract_model_fields(model)
    
    @staticmethod
    def _generate_model_name(model: Any) -> str:
        return re.sub(r'(?<!^)(?=[A-Z])', '_', model.__name__).lower()
    
    @staticmethod
    def _extract_model_fields(model: Any) -> List[str]:
        return [attr for attr in dir(model) if not callable(getattr(model, attr)) and not attr.startswith("_")]

    def _validate_model_field(self, field_name: str):
        if field_name not in self._model_fields:
            raise ValueError(f"The field '{field_name}' does not exist in the model '{self._model_name}'")

    def _validate_operator(self, operator: str):
        if operator not in self.ALLOWED_OPERATORS:
            raise ValueError(f"The operator '{operator}' is not allowed. Allowed operators are: {', '.join(self.ALLOWED_OPERATORS)}")

    def convert(self, params: dict):
        if params is None:
            return {"fields": [], "filters": [], "sort": [], "page_offset": 0, "page_size": 10}

        convertd = {}
        convertd["fields"] = self._extract_fields(params)
        convertd["filters"] = self._extract_filters(params)
        convertd["sort"] = self._extract_sorts(params)
        convertd["page_offset"] = int(params.get("page[offset]", 0))
        convertd["page_size"] = int(params.get("page[size]", 10))
        return convertd
    
    def _extract_fields(self, params: dict) -> List[str]:
        fields_key = f"fields[{self._model_name}]"
        if fields_key not in params or params[fields_key] == "":
            return []
        
        fields = params[fields_key].split(',')
        for field_name in fields:
            self._validate_model_field(field_name)
        return fields

    def _extract_filters(self, params: dict) -> List[dict]:
        filters = []
        for key, value in params.items():
            if "filter" in key:
                parts = key.split('[')
                field_name = parts[1].replace(']', '')
                operator = parts[2].replace(']', '')
                self._validate_model_field(field_name)
                self._validate_operator(operator)
                filters.append({"key": field_name, "operator": operator, "value": value})
        return filters

    def _extract_sorts(self, params: dict) -> List[dict]:
        if "sort" not in params:
            return []
        
        sorts = []
        for field_name in params.get("sort", "").split(','):
            order = "asc"
            if field_name.startswith('-'):
                order = "desc"
                field_name = field_name[1:]
            self._validate_model_field(field_name)
            sorts.append({"key": field_name, "order": order})
        return sorts
