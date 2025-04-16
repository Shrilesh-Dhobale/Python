class Test:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fun(self):
        print("Hi")

t=Test(10,20)
print(t.x)
print(t.y)
t.fun()