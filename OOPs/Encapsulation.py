class Date:
    def __init__(self,dd,mm,yyyy):
        self.__dd=dd
        self.__mm=mm
        self.__yyyy=yyyy

    def get(self):
        return f"{self.__dd}/{self.__mm}/{self.__yyyy}"