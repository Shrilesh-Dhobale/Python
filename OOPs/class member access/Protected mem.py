class Test:
    def __init__(self,x,y):
        self._x=x
        self.y=y
    def _fun(self):
        print("hi")
t=Test(10,20)
print(t._x)
print(t.y)
t._fun()