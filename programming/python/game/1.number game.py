import random
import os
'''
1. 숫자를 입력받는다.
2. 정답이면 정답이라 출력한다.
3. 틀리면 틀렸다 출력한다.
'''
def input_check(casting=int):
    while True:
        try:
            user_input = casting(input("몇 일까요?"))
            return user_input
        except:
            print("숫자만 입력하세요!")
            continue

chance = 10
count = 0
number = random.randint(1,99)

while count < chance:
    count += 1
    user_input = input_check()
    if number == user_input:
        break
    elif number > user_input:
        print(f"{user_input}보다 큰 숫자 입니다.")
    elif number < user_input:
        print(f"{user_input}보다 작은 숫자 입니다.")

if number == user_input:
    print(f"정답! {number}이 정답입니다!")
else:
    print(f"실패! 정답은 {number}입니다 ㅠㅠ")