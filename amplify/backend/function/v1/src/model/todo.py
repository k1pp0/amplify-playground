import json


class Todo:
    def __init__(self, **kwargs):
        self.__todo_id = kwargs.get('todo_id')
        self.__title = kwargs.get('title')
        self.__description = kwargs.get('description')
        self.__due_date = kwargs.get('due_date')
        self.__is_completed = kwargs.get('is_completed', False)

    @property
    def todo_id(self):
        return self.__todo_id
    
    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def due_date(self):
        return self.__due_date

    @property
    def is_completed(self):
        return self.__is_completed

    def mark_as_completed(self):
        self.__is_completed = True

    def mark_as_incomplete(self):
        self.__is_completed = False

    def __str__(self):
        status = "Completed" if self.__is_completed else "Incomplete"
        return f"Todo ID: {self.__todo_id}\nTitle: {self.__title}\nDescription: {self.__description}\nDue Date: {self.__due_date}\nStatus: {status}"

    def to_json(self):
        return json.dumps({
            "todo_id": self.__todo_id,
            "title": self.__title,
            "description": self.__description,
            "due_date": self.__due_date,
            "is_completed": self.__is_completed
        })
        