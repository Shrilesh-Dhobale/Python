class Complex:

    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def print(self):
        print(str(self.real)+"+"+str(self.imag)+"i")

    def add(self,c):
        self.real += c.real
        self.imag += c.imag 

c1=Complex(10,20)
c1.print()

c2=Complex(20,30)
c1.add(c2)
c1.print()
        