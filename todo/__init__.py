class Todo:
    def __init__(self, code_id: int, title: str, description: str, completed: bool = False, tags: list[str] = None):
        self.code_id = code_id
        self.title = title
        self.description = description
        self.completed = completed
        self.tags = tags

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag is not self.tags:
            self.tags.append(tag)
