import random
import os

chance = 10
count = 0

def input_check(casting=int):
    while True:
        try:
            user_input = casting(input('숫자를 맞혀보세요! : '))
            return user_input
        except:
            print('숫자만 입력 가능합니다!')
            continue


answer = random.randint(1, 99)
os.system('cls')
print('1부터 99까지의 수를 10번 안에 맞춰 보세요 :)')

while count < chance:
    try:
        user_input = input_check()
        if answer == user_input:
            break
        elif answer > user_input:
            count+=1
            print(f'아닙니다! {user_input}보다 큽니다. {chance-count}번 남았습니다.')
        elif answer < user_input:
            count+=1
            print(f'아닙니다! {user_input}보다 작습니다. {chance-count}번 남았습니다.')
    except ValueError:
        print('숫자만 입력하세요:) ')

if user_input == answer:
    print(f"성공! {answer}이 맞습니다.")
else:
    print(f"실패, {answer}이 정답입니다.")