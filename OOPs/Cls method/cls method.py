class Employee:
    compName = "gfg"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @classmethod
    def set_compName(cls,cName):
        cls.compName=cName

Employee.set_compName("Geeks for Geeks")
print(Employee.compName)

e=Employee("Sandip",23)
print(Employee.compName)

