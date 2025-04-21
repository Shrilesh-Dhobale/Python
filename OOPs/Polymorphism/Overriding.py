class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def printDetails(self):
        print(self.id)
        print(self.name)

class SalesEmployee(Employee):
    def __init__(self,id,name,sales_incentive):
        super().__init__(id,name)
        self.sales_Inc=sales_incentive
    def printDetails(self):
        super().printDetails()
        print(self.sales_Inc)

el=[Employee(101,"Sandip",),SalesEmployee(101,"Akash",50000)]

for x in el:
    x.printDetails()