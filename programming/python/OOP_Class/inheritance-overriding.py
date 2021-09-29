class Robot:
    """
    [Robot Class]
    Date : ??:??:??
    Author : Amaco
    """

    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."

    @staticmethod
    def are_you_robot():
        print(f"{Robot.population} num!")
        print("yes!!")

    def __str__(self):
        return f"{self.name} robot!!"

    def __call__(self):
        print("call!")
        return f"{self.name} call!!"


class Siri(Robot):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Siri.population += 1  # class variable

    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        self.a = a
        return a * b

    @classmethod
    def hello_apple(cls):
        print(f"{cls} hello apple!")

    def say_hi(self):  # method overriding
        print(f"Greetings, my masters call me{self.name}. by apple.")

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots. by apple"


siri = Siri("iphone8", 17)

siri.say_hi()
print(Siri.how_many())  # We have 1 robots. by apple >> overriding

print(Siri.__dict__)
