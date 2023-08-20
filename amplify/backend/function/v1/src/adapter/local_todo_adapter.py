from model.todo import Todo
from interface.adapter.i_todo_adapter import ITodoAdapter


class LocalTodoAdapter(ITodoAdapter):
    def __init__(self):
        self.todo_data = []
        for i in range(10):
            self.todo_data.append(Todo(
                todo_id=f"id_{i}",
                title=f"Task {i}",
                description=f"Description for Task {i}",
                due_date=f"2023-08-{10+i}"
            ))
    
    def read(self, todo_id: str) -> Todo:
        existing_todo = next((todo for todo in self.todo_data if todo.todo_id == todo_id), None)
        if existing_todo:
            return existing_todo
        else:
            raise ValueError(f"Todo with ID {todo_id} not found.")
