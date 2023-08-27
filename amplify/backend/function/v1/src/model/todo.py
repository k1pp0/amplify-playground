import json


class Todo:
    def __init__(self, **kwargs):
        self._todo_id = kwargs.get('todo_id')
        self._title = kwargs.get('title')
        self._description = kwargs.get('description')
        self._due_date = kwargs.get('due_date')
        self._is_completed = kwargs.get('is_completed', False)

    @property
    def todo_id(self):
        return self._todo_id
    
    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def due_date(self):
        return self._due_date

    @property
    def is_completed(self):
        return self._is_completed

    def mark_as_completed(self):
        self._is_completed = True

    def mark_as_incomplete(self):
        self._is_completed = False

    def __str__(self):
        status = "Completed" if self._is_completed else "Incomplete"
        return f"Todo ID: {self._todo_id}\nTitle: {self._title}\nDescription: {self._description}\nDue Date: {self._due_date}\nStatus: {status}"

    def to_dict(self):
        return {
            "todo_id": self._todo_id,
            "title": self._title,
            "description": self._description,
            "due_date": self._due_date,
            "is_completed": self._is_completed
        }
