class Employee:
    compName="Tata"
    def __init__(self,id):
        self.id=id
    def fun(self,n):
        self.name=n
e=Employee("1003")
e.fun("Harry")
print(e.name)

e.designation="Developer"
print(e.designation)

Employee.officeAdd="Delhi"
print(e.officeAdd)