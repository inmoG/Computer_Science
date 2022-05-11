'''
영어단어 맞추기
딕셔너리로 영어 단어장을 만든다. 
단어만 모은 리스트를 만든다.
단어를 섞는다
단어를 보여주면 단어 뜻을 맞춘다.
정답이면 정답을 출력한다
틀리면 다음 단어를 보여준다.
기회가 다 소진되면 맞춘 개수를 출력한다.
'''
import random

words_list = {
    '사과':'apple',
    '사자':'lion',
    '호랑이':'tiger'
}

words = []
count = 0
chance = 3

for key in words_list:
    words.append(key)

random.shuffle(words)
length = len(words)

for word in words:
    for cnt in range(length):
        user_input = str(input(f'{word}의 뜻을 맞춰보세요 :) '))
        if words_list[word] == user_input:
            print(f'{words_list[word]} 정답입니다!')
            count+=1
            break # for문을 종료해 다음 단어를 출력한다.
        else:
            print(f'틀렸습니다!')
    if words_list[word] != user_input:
        print(f"{word}의 뜻은 {words_list[word]}입니다!")

print(f'총 {count}개 맞췄습니다')





























'''
words_dict = {
    "사자": 'lion',
    '호랑이': 'tiger',
    '사과': 'apple',
    '비행기': "airplane"
}

words = []

for word in words_dict:  
    words.append(word) # append dict key

random.shuffle(words) # 순서 섞기

chance = 3
for i in range(0, len(words)):
    q = words[i] # key를 q에 담는다.

    for j in range(0, chance):
        user_input = str(input(f"{q}의 영어단어를 입력하세요 > ")) # ex 사자의 영어 단어를 입력하세요
        english = words_dict[q] # get value

        if user_input.strip().lower() == english.lower():
            print('정답 입니다.')
            break
        else:
            print('틀렸습니다.')

    if user_input != english: # 정답을 못맞췄을 경우
        print(f'정답은 {english}입니다.')

print('모든 문제를 풀었습니다.')

'''
