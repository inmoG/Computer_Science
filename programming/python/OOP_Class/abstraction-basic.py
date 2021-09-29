"""
추상화 : abstraction
불필요한 정보는 숨기고 중요한(필요한) 정보만을 표현함으로써
공통의 속성 값이나 행위(methods)를 하나로 묶어 이름을 붙이는 것이다.

인스턴스는 독립적이다.
클래스 공간과 인스턴스 공간은 분리되어 있다.
인스턴스에서 클래스는 접근 가능하나 클래스에서 인스턴스 공간은 접근 X
"""


class Robot:

    population = 0  # 클래스 변수 : 인스턴스들이 공유하는 변수

    def __init__(self, name, code):  # 생성자 함수
        self.name = name  # 인스턴스 변수
        self.code = code  # 인스턴스 변수
        Robot.population += 1  # 클래스 변수는 인스턴스가 공유할 수 있어서 접근 가능하다.

    # instance method
    def say_hi(self):
        # code
        print(f"Greetings, my basters call me {self.name}.")

    # instance method
    def cal_add(self, a, b):
        return a + b

    # instance method
    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one")
        else:
            print(f"There are still {Robot.population} robots working.")

    @classmethod
    def how_many(cls):  # cls >> class??
        print(f"we have {cls.population} robots.")


print(Robot.population)  # 0

siri = Robot("siri", 2020202020)

print(Robot.population)  # 1

jarvis = Robot("jarvis", 233232323)

print(Robot.population)

bixby = Robot("bixby", 124312423)

print(Robot.population)  # 3

bixby2 = Robot("bixby2", 124312423)
bixby23 = Robot("bixby2", 124312423)

print(siri.name)
# print(siri.code)

jarvis.say_hi()

jarvis.die()

Robot.how_many()
