class Employee:
    compName="TCS"

    def __init__(self,id):
        self.id=id

e1=Employee(1001)
e2=Employee(1002)

Employee.compName="Infosys"

print(e1.compName)
print(e2.compName)
