from typing import List

from model.todo import Todo
from interface.adapter.i_todo_adapter import ITodoAdapter


class LocalTodoAdapter(ITodoAdapter):
    def __init__(self):
        self._todo_data = []
        for i in range(10):
            self._todo_data.append(Todo(
                todo_id=f"id_{i}",
                title=f"Task {i}",
                description=f"Description for Task { 'Odd' if i % 2 == 1 else 'Even' }",
                due_date=f"2023-08-{10+i}"
            ))
    
    def read(self, todo_id: str) -> Todo:
        existing_todo = next((todo for todo in self._todo_data if todo.todo_id == todo_id), None)
        if existing_todo:
            return existing_todo
        else:
            raise ValueError(f"Todo with ID {todo_id} not found.")
    
    def list(self, params: dict) -> List[Todo]:

        def filter_and_sort_data(data, params):
            def apply_filters(item):
                for filter_item in params.get("filters", []):
                    key = filter_item["key"]
                    operator = filter_item["operator"]
                    value = filter_item["value"]
                    current_value = getattr(item, key)
                    
                    conditions = {
                        "eq": current_value == value,
                        "ne": current_value != value,
                        "lt": current_value < value,
                        "le": current_value <= value,
                        "gt": current_value > value,
                        "ge": current_value >= value,
                        "in": current_value in value,
                        "nin": current_value not in value,
                        "like": value in current_value,
                        "ilike": value.lower() in current_value.lower(),
                        "startswith": current_value.startswith(value),
                        "endswith": current_value.endswith(value),
                        "isnull": current_value is None,
                        "notnull": current_value is not None
                    }
                    
                    if not conditions.get(operator, False):
                        return False

                return True

            filtered_data = list(filter(apply_filters, data))
            
            sorts = params.get("sorts", [])
            for sort in reversed(sorts):
                filtered_data.sort(key=lambda x: getattr(x, sort["key"]), reverse=(sort["order"] == "desc"))
            
            page_offset = params.get("page_offset", 0)
            page_size = params.get("page_size", len(filtered_data))
            paginated_data = filtered_data[page_offset: page_offset + page_size]
            
            fields = params.get("fields", [])
            final_data = [{field: getattr(item, field) for field in fields} for item in paginated_data]

            return final_data

        todos: List[Todo] = filter_and_sort_data(self._todo_data, params)
        return todos
