import random
import os
'''
변수 - chance, count, number(정답), user_input
1. 숫자를 입력받는다.

2. 숫자인지 문자인지 확인한다.

3. 숫자이면 
3-1. 카운트를 증가한다.
3-2. 정답인지 확인한다.
3-3. 정답이면 반복문을 탈출한다.
3-4. 틀리면 힌트를 출력한다.
3-4-1. 입력값이 정답보다 크면 입력값이 크다고 출력한다.
3-4-2. 입력값이 정답보다 작으면 입력값이 작다고 출력한다.

4. 문자면
4-1. 다시 숫자를 입력하라 출력한다.

5. 기회를 다 소진하면 실패, 정답을 출력한다.
6. 정답이면 축하한다 출력한다.

'''

os.system("cls")

chance = 10
count = 0
number = random.randint(1, 99)

def input_check(casting=int):
    while True:
        try:
            user_input = casting(input("숫자를 입력하세요 ! "))
            return user_input
        except:
            print("숫자만 입력하셔야 합니다..!")
            continue

while count < chance:
    user_input = input_check()
    count+=1
    print(f"남은 기회는 {chance-count}입니다.")

    if number == user_input:
        break
    elif number > user_input:
        print(f"{user_input}보다 큰 숫자입니다!")
    elif number < user_input:
        print(f"{user_input}보다 작은 숫자입니다!")

if number == user_input:
    print(f"{number}이 정답입니다!")
else:
    print(f"실패!! {number}가 정답입니다 ㅠㅠ")

