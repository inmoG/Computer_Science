import os

operator = ["+", "-", "*", "/", "="]

'''
operator user_input string_list 
1. 빈 리스트를 생성한다.
2. 
'''


def string_calculator(user_input, show_history=False):
    string_list = []
    lop = 0

    if user_input[-1] not in operator:
        user_input += "="

    for i,s in enumerate(user_input): # index, values
        if s in operator:
            if user_input[lop:i].strip() != "":
                string_list.append(user_input[lop:i]) # append only number
                string_list.append(s) # append operator

                lop = i+1 # next number index 
    string_list = string_list[:-1]
    print(string_list)
    pos = 0
    while True:
        if pos + 1 > len(string_list):
            break
        if len(string_list) > pos + 1 and string_list[pos] in operator: # 개수 > 현재위치 + 1 and 연산자
            temp = string_list[pos-1] + string_list[pos] + string_list[pos+1] # 숫자 + 연산자 + 숫자
            del string_list[0:3]
            string_list.insert(0, str(eval(temp)))
            pos = 0

            if show_history:
                print(string_list)
        pos += 1

    if len(string_list) > 0:
        result = float(string_list[0])

    return round(result, 4)



#while True:
os.system("clear")
user_input = input("계산식을 입력하세요 > ")

    #if user_input == "/exit":
    #    break
result = string_calculator(user_input, show_history=True) # [60-30]
print(f"결과 {result}")
