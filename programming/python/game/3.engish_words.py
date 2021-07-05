import random

'''
1. 영어단어 딕셔너리를 만든다.
2. 빈 리스트에 딕셔너리의 키를 추가한다.
3. 리스트를 섞는다.
4. 기회를 설정한다.
5. 단어개수만큼 문제를 반복한다.
    7. 리스트에서 키를 구한다.    
        6. 주어진 기회동안 1문제를 반복한다.
        8.  정답을 입력받는다.
        9. 딕셔너리에서 값을 구한다.
        10. 입력값과 정답을 소문자로 변환한다.
        11. 정답이라면 정답이라 출력하고 반복문을 탈출한다.
        12. 틀리면 주어진 기회만큼 문제를 반복해 제출한다.
    13. 기회동안 문제를 못 풀면 정답을 출력한다.
14. 문제를 모두 다 풀면 게임을 종료한다 출력한다.
'''

words_dict = {
    "사자": "lion",
    "호랑이": "tiger",
    "사과": "apple",
    "비행기": "airplane"
}

words = []

for i in words_dict:
    words.append(i)

random.shuffle(words)

chance = 3

for i in range(0, len(words)):
    q = words[i] # q << words.사자
    for i in range(0, chance):
        user_input = str(input(f"{q}의 정답을 입력하세요 !! "))
        answer = words_dict[q]

        if user_input.strip().lower() == answer.lower():
            print("정답입니다!!")
            break # 정답이므로 안쪽 for문 탈출해 다음 문제 제출한다.
        else:
            print("틀렸습니다") # 안쪽 for문이 끝날때까지 기회를 제공한다.
    if user_input.strip().lower() != answer.lower():
        print(f"정답은 {answer}입니다...!")

print("문제가 더 이상 없습니다, 게임 종료!")