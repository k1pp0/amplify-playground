import re
from typing import Dict, Any, List

class JsonApiDoc:

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
    
    def json_api_to_model_class_dict(self, json_api_dict: Dict[str, Any]) -> Dict[str, Any]:
        data = json_api_dict.get("data", {})
        if not data:
            raise ValueError(f"The json:api format requires a 'data' member at the top level")
        model_class_dict = {}
        if "id" in data:
            model_class_dict[f"{self._model_name}_id"] = data.pop("id")
        attributes = data.get("attributes", {})
        for field_name, value in attributes.items():
            self._validate_model_field(field_name)
            model_class_dict[field_name] = value
        return model_class_dict

    def model_class_to_json_api_dict(self, model_class_dict: Dict[str, Any]) -> Dict[str, Any]:
        json_api_dict = {"data": {"type": self._model_name}}
        id_key = f"{self._model_name}_id"
        if id_key in model_class_dict:
            json_api_dict["data"]["id"] = model_class_dict.pop(id_key)
        attributes = {}
        for field_name, value in model_class_dict.items():
            self._validate_model_field(field_name)
            attributes[field_name] = value
        if attributes:
            json_api_dict["data"]["attributes"] = attributes
        return json_api_dict