import re
from typing import Any, List

class QueryStringParameters:

    ALLOWED_OPERATORS = set([
        "eq", "ne", "lt", "le", "gt", "ge",
        "in", "nin", "like", "ilike", 
        "startswith", "endswith",
        "isnull", "notnull"
    ])

    def __init__(self, model: Any):
        self._model_name = self._generate_model_name(model)
        self._model_fields = self._extract_model_fields(model)
    
    @staticmethod
    def _generate_model_name(model: Any) -> str:
        return re.sub(r'(?<!^)(?=[A-Z])', '_', model.__name__).lower()
    
    @staticmethod
    def _extract_model_fields(model: Any) -> List[str]:
        return [attr for attr in dir(model) if not callable(getattr(model, attr)) and not attr.startswith("__")]

    def _validate_model_field(self, field_name: str):
        if field_name not in self._model_fields:
            raise ValueError(f"The field '{field_name}' does not exist in the model '{self._model_name}'")

    def _validate_operator(self, operator: str):
        if operator not in self.ALLOWED_OPERATORS:
            raise ValueError(f"The operator '{operator}' is not allowed. Allowed operators are: {', '.join(self.ALLOWED_OPERATORS)}")

    def convert(self, params: dict):
        convertd = {}
        
        fields_key = f"fields[{self._model_name}]"
        if fields_key in params:
            convertd["fields"] = params[fields_key].split(',')
            for field_name in convertd["fields"]:
                self._validate_model_field(field_name)
        
        convertd["filters"] = self._extract_filters(params)
        convertd["sorts"] = self._extract_sorts(params)
        convertd["page_offset"] = int(params.get("page[offset]", 0))
        convertd["page_size"] = int(params.get("page[size]", 10))

        return convertd

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
        sorts = []
        for field_name in params.get("sort", "").split(','):
            order = "asc"
            if field_name.startswith('-'):
                order = "desc"
                field_name = field_name[1:]
            self._validate_model_field(field_name)
            sorts.append({"key": field_name, "order": order})
        return sorts
