class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(f"Student:{self.name},ID:{self.id}")

class Programmer(Student):
    def showLang(self):
        print("Python is one of the famous lang")

e1=Student("Rohan",343)
e1.show()
e2=Programmer("Anay",344)
e2.show()
e2.showLang()