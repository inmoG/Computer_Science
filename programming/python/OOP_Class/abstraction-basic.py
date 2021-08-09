"""
추상화 : abstraction
불필요한 정보는 숨기고 중요한(필요한) 정보만을 표현함으로써
공통의 속성 값이나 행위(methods)를 하나로 묶어 이름을 붙이는 것이다.

인스턴스는 독립적이다.
클래스 공간
인스턴스 공간
"""


class Robot:
    # class 변수 : 인스턴스들이 공유하는 변수
    population = 0

    # 생성자 함수 : 초기화를 시켜주는 함수
    def __init__(self, name, code):
        self.name = name  # instance 변수
        self.code = code
        Robot.population += 1

    # 인스턴스 메서드
    def say_hi(self):
        print(f"hi {self.name}")

    def cal_add(self, a, b):
        return a + b

    def die(self):
        print(f"{self.name} die die!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one")
        else:
            print(f"There are still {Robot.population} robots working")

    # class 메서드
    @classmethod
    def how_many(cls):  # cls는 class를 받는다
        print(f"we have {cls.population} robots")


print(Robot.population)  # 0

siri = Robot("siri", 1231231233)
print(Robot.population)  # 1

jarvis = Robot("jarvis", 132145425425)
print(Robot.population)  # 2
bixby = Robot("bixby", 123515135)
print(Robot.population)  # 3

print(siri.name)
print(siri.code)

siri.say_hi()
siri.cal_add(2, 3)

Robot.how_many()
siri.die()
jarvis.die()
bixby.die()
# siri_name = "siri"
# siri_code = 2123131321
#
#
# def siri_say_hi():
#    # code...
#    print("say hello!! my name is siri")
#
#
# def siri_add_cal():
#    return 2 + 3
#
#
# def siri_die():
#    print("siri die")
#
#
# javis_name = "javis"
# javis_code = 12345255
#
