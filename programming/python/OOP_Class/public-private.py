"""
* public vs private

__age : private 변수 외부에서 접근이 불가능하다. 함수에도 적용 가능!
"""


class Robot:

    """
    Robot Class
    """

    population = 0

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        Robot.population += 1

    def __say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."


class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name, age)
        print(self.name)
        print(self.__age)  # age has no
        # self.__age = 999
        # print(self.__age) 999


ss = Robot("yss", 8)

# ss.age

# ss.age = -999

ssss = Siri("iphone8", 9)
