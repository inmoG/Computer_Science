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

    @staticmethod
    def this_is_robot_class():
        print("yes!!")


siri = Robot("siri", 13213213)

print(Robot.this_is_robot_class())
print(siri.this_is_robot_class())

"""
class Cal:
    # 생성자 : 메모리에 올라오는 순간 즉시 실행되는 함수
    def __init__(self, a, b):
        self.a = a  # instance 변수
        self.b = b

    def add(self):  # 인스턴스 메서드
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


cal1 = Cal(2, 3)
cal2 = Cal(3, 4)

print(cal1.a)
print(cal1.b)
print(cal1.add())

print(cal2.a)
print(cal2.b)

cal1.a = 7

print(cal1.add())

"""
