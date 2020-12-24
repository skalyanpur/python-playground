from typing import Optional, List


class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student(name="bob")
cat = Student(name="cat")

bob.take_exam(90)
# cat.take_exam(100)

print(bob.grades)
print(cat.grades)
