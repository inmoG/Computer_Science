"""
#* [property]
#* 인스턴스 변수 값을 사용해서 적절한 값으로 보내고 싶을 때
#* 인스턴스 변수 값에 대한 유효성 검사 및 수정
"""


class Robot:

    """
    Robot Class
    """

    __population = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Robot.__population += 1

    @property
    def name(self):
        return f"yoon {self.__name}"

    @property  # 접근하여 함수 사용은 가능하나 수정은 불가능하다.
    def age(self):
        return self.__age

    @age.setter  # 접근하여 수정 가능
    def age(self, new_age):
        if new_age - self.__age == 1:  # 변수 유효성 검사
            self.__age = new_age
        else:
            raise ValueError()

    def __say_hi(self):
        print(f"Greetings, my masters call me {self.__name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.__population} robots."


droid = Robot("R2-D2", 2)

print(droid.age)

# droid.age = 7 수정 불가능
droid.age += 1

print(droid.age)
print(droid.name)
