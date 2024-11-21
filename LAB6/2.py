class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks  # Protected attribute

    def update_marks(self, new_marks):
        self._marks = new_marks
