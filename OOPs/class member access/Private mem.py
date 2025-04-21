class Test:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    def __fun(self):
        print("Hi")
t=Test(10,20)
print(t._Test__x)
print(t._Test__y)
t._Test__fun()

        