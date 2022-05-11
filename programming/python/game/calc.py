import os

while True:
    os.system('cls')
    s = input('계산기 입력 > ')
    print(eval(s)) # string을 계산가능하게 바꿔준다.
    os.system('pause')