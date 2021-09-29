# decorator


def copyright(func):
    def new_func():
        print("@ amamovsdfjkldjsakfljdskaljfkdsla")  # 2. 출력
        func()  # 3. func() > smile() 실행

    return new_func  # 1 new_func 실행


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
