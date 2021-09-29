"""
namespace == 개체를 구분할 수 있는 범위
__dict__ == 네임스페이스를 확인할 수 있다
dir() == 네임스페이스 key값을 확인할 수 있다
__doc__ == class 주석을 확인한다
__class__ == 어떤 클래스로 만들어진 인스턴스인지 확인할 수 있다.
"""


class Robot:
    """
    [Robot class]
    Author : 양인모
    Role : ???
    """

    # class varialbe : 인스턴스들이 공유하는 변수
    population = 0

    # 생성자 함수
    def __init__(self, name):
        self.name = name  # instance variable
        Robot.population += 1  # class 변수는 인스턴스가 공유하는 변수라 접근 가능하다.
        # self로는 접근 X class로만 접근할 수 있다.

    # instance method
    def say_hi(self):
        # code
        print(
            f"Greetings, my masters call me {self.name}"
        )  # 인스턴스 공간에 있으므로 self로 name 변수 접근 가능하다.

    def cal_add(self, a, b):
        return a + b

    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one")
        else:
            print(f"There are still {Robot.population} robots working")

    @classmethod
    def how_many(cls):  # 인스턴스 메서드 상태에서 왜 cls가 먹히지? 인스턴스는 클래스 메서드도 호출할 수 있는가?
        print(f"we have {cls.population} robots")


siri = Robot("siri")
jarvis = Robot("jarvis")
bixby = Robot("bixby")

print(Robot.__dict__)
print(siri.__dict__)
print(jarvis.__dict__)


print(siri.name)
print(bixby.name)

print(siri.cal_add(2, 3))  # 인스턴스 네임스페이스에 해당 함수가 없는데 쓸 수 있는 이유는 클래스에 접근해 가져오기 때문?

print(siri.population)

siri.how_many()
# Robot.how_many()

Robot.say_hi(siri)
# Robot.say_hi() >> TypeError: say_hi() missing 1 required positional argument: 'self'
siri.say_hi()

print(dir(siri))  # __dict__랑 dir은 왜 결과가 다른걸까?
print(dir(Robot))  # dir에서 Robot은 인스턴스 메서드를 가지고 있지 않다. 그러나 __dict__에서는 갖고 있다.

print(Robot.__doc__)
print(jarvis.__class__)
