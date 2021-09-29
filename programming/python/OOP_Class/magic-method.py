class Robot:
    """
    Robot class
    Date : ?????
    Author : inmo
    """

    population = 0

    def __init__(self, name):  # 생성자 함수
        self.name = name  # instance variable
        Robot.population += 1  # class variable

    def die(self):
        print(f"{self.name} is being destroyed")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one")
        else:
            print(f"there are still {Robot.population} robots working")

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):  # classmethod >> cls
        return f"we have {cls.population} robots"

    @staticmethod  # instance, class 개체 모두 접근이 가능하다.
    def are_you_robot():
        print("yes!")

    def __str__(self):
        return f"{self.name} robot!!"

    def __call__(self):
        print("call!!")
        return f"{self.name} call!!"


droid = Robot("r2-d2")
droid.say_hi()

print(dir(droid))
# print(droid)  # <__main__.Robot object at 0x7ff00b3190a0> >> rs-d2 robot!!

droid()  # 함수처럼 호출이 가능하다?

droid.are_you_robot()
Robot.are_you_robot()
