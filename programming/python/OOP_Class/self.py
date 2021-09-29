# self 이해
# self는 인스턴스 객체이다.
# 클래스 안에 있는 self 주소와 만들어진 인스턴스 주소는 같다. 즉 self는 인스턴스 그 자체이다.


class SelfTest:
    # class variable
    name = "inmo"

    def __init__(self, x):
        self.x = x  # instance variable

    # class method
    @classmethod
    def func1(cls):
        print(f"cls: {cls}")
        print(f"class 주소 : ", id(cls))
        print("func1")

    # instance method
    def func2(self):
        print(f"self : {self}")
        print("class 안의 self 주소 : ", id(self))
        print("func2")


test_obj = SelfTest(17)

SelfTest.func1()  # class method
test_obj.func2()  # instance method
print(id(test_obj))  # 만들어진 인스턴스 주소
# SelfTest.func2()
# print(SelfTest.x)

test_obj.func1()  # class method
print(test_obj.name)  # class variable


"""
class안의 self 주소 140615589766144
func2
cls:<class '__main__.SelfTest'>     >> cls는 클래스 그 자체를 가리킨다.
func1
인스턴스 주소 :  140615589766144
"""
