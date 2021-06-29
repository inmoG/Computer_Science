import random

'''
 1. 컴퓨터가 숫자 3개를 만든다.
 2. 유저에게 숫자 3개 입력받는다.
 3. 숫자인지 문자인지 확인한다.
 4. 숫자가 3개인지 확인한다.
 5. 볼인지 스트라이크인지 확인한다.
 6. 스트라이크면 스트라이크 증가
 7. 볼이면 볼 증가
 8. 둘 다 아니면 삼진아웃
 8-1. 스트라이크가 0보다 크면 스트라이크 출력
 8-2. 볼이 0보다 크면 볼 출력
 9. 3스트라이크면 게임 종료
'''

numbers = []
number = random.randint(0,9)
for i in range(3):
    while number in numbers:
        number = str(random.randint(0,9))
    numbers.append(number)

def input_check():
    while True:
        try:
            user_input = str(input("숫자 3개 입력하세요!"))
            return user_input
        except:
            print("문자는 안됩니다. 숫자를 입력하세요!")
            continue

count_strike = 0
count_ball = 0


while count_strike < 3:
    count_strike = 0 # 반복문안에서 0으로 초기화 해야 입력할때마다 입력된 값을 비교할 수 있게 됩니다.
    count_ball = 0

    user_input = input_check()
    if len(user_input) == 3:
        for i in range(0, 3):
            for j in range(0, 3):
                if numbers[i] == user_input[j] and i == j:
                    count_strike += 1
                elif numbers[i] == user_input[j] and i != j:
                    count_ball += 1
        if count_ball == 0 and count_strike == 0:
            print("삼진 아웃!!")
        else:
            output = ""
            if count_strike > 0:
                print(f"{count_strike} 스트라이크 !!")
            if count_ball > 0:
                print(f"{count_ball} 볼!!") 

print("게임 종료! ")






























'''
def input_check():
    while True:
        try:
            user_input = str(input("숫자 3개를 입력하세요"))
            return(user_input)
        except:
            print("숫자를 입력하세요!!")
            continue

numbers = []
number = str(random.randint(0, 9))

for i in range(3):
    while number in numbers: # list에 number 값이 있다면 true >> 반복문 진입
        number = str(random.randint(0, 9)) # number 초기화 
    numbers.append(number)

os.system("cls")

print("*" * 60)
print("야구게임을 시작 합니다!!!")
print("*" * 60)

count_strike = 0
count_ball = 0

while count_strike < 3:
    count_strike = 0
    count_ball = 0

    num = str(input("숫자 3자리 입력하세요 > "))
    if len(num) == 3:
        for i in range(0, 3):
            for j in range(0, 3):
                if num[i] == numbers[j] and i == j: # 숫자 and 자리값
                    count_strike +=1
                elif num[i] == numbers[j] and i != j:
                    count_ball += 1
        if count_strike == 0 and count_ball == 0:
            print("3 아웃!! ")
        else:
            output = ""
            if count_strike > 0:
                output += f"{count_strike}스트라이크"
            if count_ball > 0: 
                output += f"{count_ball} 볼!"

            print(output.strip)
print("게임 성공")
'''