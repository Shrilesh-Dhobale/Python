class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def printDetails(self):
        print(self.id)
        print(self.name)

class Employee(Person):
    def __init__(self,name,id,sal):
        super().__init__(name,id)
        self.sal=sal
    def printDetails(self):
        super().printDetails()
        print(self.sal)

class salesEmployee(Employee):
    def __init__(self,name,id,sal,si):
        super().__init__(name,id,sal)
        self.salesinc=si
    def printDetails(self):
        super().printDetails()
        print(self.salesinc)

se=salesEmployee(101,"Rahul",30000,2000)
e=Employee("Sanay",124,30000)

se.printDetails()
e.printDetails()
