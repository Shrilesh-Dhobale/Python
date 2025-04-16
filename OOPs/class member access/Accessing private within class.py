class Test:
    def __init__(self,x):
        self.__x=x
        self.__y=10
    def printTest(self):
        print(self.__x)
        print(self.__y)

t=Test(5)
t.printTest()