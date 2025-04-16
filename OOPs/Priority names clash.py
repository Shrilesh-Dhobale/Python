class Employee:
    compName="JP"

    def __init__(self,id):
        self.id=id

e=Employee(1001)
Employee.officeAdd="Noida"

e.officeAdd="NCR"
print(Employee.officeAdd)
print(e.officeAdd)