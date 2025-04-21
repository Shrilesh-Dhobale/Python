class Person:
    def __init__(self,id,name):
        self.id=id
        self.name=name
class Student(Person):
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def printDetails(self):
        print("Student:")
        print(self.id)
        print(self.name)
class Faculty(Person):
    def __init__(self,id,name):
        super().__init__(id,name)
    def printDetails(self):
        print("Faculty:")
        print(self.id)
        print(self.name)
class PhDStudent(Student,Faculty):
    def __init__(self,id,name):
        super().__init__(id,name)

bs=PhDStudent(101,"Sandub")
bs.printDetails
