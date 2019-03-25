class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return repr(self.name)


class Student(Person):
    def __init__(self, name, college_name, year):
        super().__init__(name)
        self.college_name = college_name
        self.year = year

    def __repr__(self):
        return repr((super().__repr__(), self.college_name, self.year))


person = Person('anil')
student = Student('anil', 'Bangalore University', 2008)

print(student)