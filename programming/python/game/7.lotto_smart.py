'''
1. 특정 숫자를 포함해서 로또 번호를 생성해주는 기능
2. 특정 숫자를 제외해서 로또 번호를 생성해주는 기능
3. 정해진 자리수만큼 연속 숫자를 포함하는 번호를 생성하는 기능
'''

import numpy

def make_lotto_number(**kwargs):
    rand_number = numpy.random.choice(range(1,46), 6, replace=False)
    rand_number.sort
    #최종 로또 번호가 완성될 변수
    lotto = []

    # 1. 특정 숫자를 포함해서 로또 번호를 생성해주는 기능
    if kwargs.get("include"): # 입력인자가 include라면
        include = kwargs.get("include") 
        lotto.extend(include) # [[1,2,3]] >>   [1,2,3]

        cnt_make = 6-len(lotto) # n개만 만든다
        for _ in range(cnt_make):
            for j in rand_number: # [1,2,3,4,5,6]
                if lotto.count(j) == 0: # n이 없다면 n을 추가한다
                    #print(f"lotto : {lotto}")
                    lotto.append(j)
                    #print(f"lotto : {lotto}")
                    break
    else: # 입력인자가 없다면
        lotto.extend(rand_number)
        #print(f"rand_number: {rand_number}")

    if kwargs.get("exclude"):
        exclude = kwargs.get("exclude")
        lotto = list(set(lotto) - set(exclude)) # 차집합
        #print(f"lotto:{lotto}")

        while len(lotto) != 6:
            for _ in range(6-len(lotto)):
                rand_number =numpy.random.choice(range(1,46), 6, replace=False)
                rand_number.sort()
                #print(f"rand_number {rand_number}")

                for j in rand_number:
                    if lotto.count(j) == 0 and j not in exclude:
                        lotto.append(j)
                        break

    if kwargs.get("continuty"):
        continuty = kwargs.get("continuty")
        start_number = numpy.random.choice(lotto, 1)
        print(f"start : {start_number}")
        seq_num = []

        for i in range(start_number[0], start_number[0] + continuty):
            seq_num.append(i) # 28,29,30
        seq_num.sort()

        lotto = []
        lotto.extend(seq_num) # lotto << [28,29,30]
        print(f"lotto : {lotto}")

        while len(lotto) != 6: # lotto 3개 != 6
            for _ in range(6 - len(lotto)):
                rand_number = numpy.random.choice(range(1, 46), 6, replace=False)
                rand_number.sort()
                print(f"rand:{rand_number}")
                for j in rand_number:
                    if lotto.count(j) == 0 and j not in seq_num:
                        lotto.append(j)
                        break
                
                lotto = list(set(lotto))


    lotto.sort()
    return lotto

lotto = make_lotto_number(continuty=3) # nclude
print(f"lotto : {lotto}")