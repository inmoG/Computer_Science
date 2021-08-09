def copyright(func):
    def new_func():
        print("@ adasdadadsad")
        func()

    return new_func


@copyright
def smile():
    print("😊")


@copyright
def angry():
    print("😒")


@copyright
def love():
    print("😍")


# smile = copyright(smile)
# angry = copyright(angry)
# love = copyright(love)

smile()
angry()
love()

"""
데코레이터 == 함수 재정의
"""
