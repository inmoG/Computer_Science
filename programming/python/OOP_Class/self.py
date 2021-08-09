class SelfTest:
    name = "amamov"

    def __init__(self, x):
        self.x = x

    # class method
    @classmethod
    def func1(cls):
        print(f"cls:{cls}")
        print("func1")

    def func2(self):
        print(f"self:{self}")
        print("class안의 self 주소", id(self))
        print("func2")


test_obj = SelfTest(17)
test_obj2 = SelfTest(19)
test_obj.func2()
SelfTest.func1()


print("인스턴스 주소 : ", id(test_obj))
print("인스턴스 주소2 : ", id(test_obj2))
test_obj2.func2()
SelfTest.func1()


"""
class안의 self 주소 140615589766144
func2
cls:<class '__main__.SelfTest'>     >> cls는 클래스 그 자체를 가리킨다.
func1
인스턴스 주소 :  140615589766144
"""

test_obj.func1()
print(test_obj.name)
