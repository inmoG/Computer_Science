import func_DML  # Data Manipulation Language와 관련된 기능들을 모아둔 파이썬 파일입니다.
import func_DDL  # Data Definition Languege와 관련된 기능들을 모아둔 파이썬 파일입니다.

func_DDL.create_table_meminfo()  # meminfo 테이블 생성


while True:
    mem_number = func_DML.memlist_information()  # meminfo 테이블에 저장된 행 수를 가져오는 함수
    print('='*30)
    print('회원관리프로그램')
    print(' 메  인  화  면')
    print('-'*30)
    print('S: 검색하기')
    print('I: 등록하기')
    print('U: 수정하기')
    print('D: 삭제하기')
    print('Q: 종료하기')
    print('현재 등록된 회원 : {}'.format(mem_number))  # DB에 몇명 등록이 되어 있는지 확인시켜주는 코드
    print('='*30)

    user_pick = input('사용할 메뉴 입력 : ')
    if user_pick.upper() == 'Q':
        print('회원관리 프로그램을 종료합니다.\n')
        break
#############등록파트############################################################################################
    elif user_pick.upper() == 'I':
        print('='*30)
        print('회원 정보 등록')
        print('-'*30)
        while True:  # 테이블을 정의한 대로 이름과 전화번호를 필수로 받아 복합키로 설정하기위한 반복문
            name = input('이    름 : ')
            if(name == ''):
                continue
            else:
                break
        age = input('나    이 : ')
        while True:
            phone = input('전화번호 : ')
            if(phone == ''):
                continue
            else:
                break
        email = input('이 메 일 : ')
        print('='*30)
        while user_pick.upper() != 'Y' or user_pick.upper() != 'N':
            user_pick = input('등록하기(Y) / 메인화면(N)  입력 : ')
            if user_pick.upper() == 'Y':
                # 이미 존재하는지 판단
                Exist = func_DML.select(name, phone)
                Exist = list(Exist)
                try:
                    if (Exist != name and Exist != phone):
                        func_DML.insert(name, age, phone, email)
                    # 데이터 삽입하는 구문
                        print(' ▶ 등록이 완료되었습니다.\n')
                        break
                except:
                        print('이미 존재하는 회원입니다.')
                        #break
                    
            elif user_pick.upper() == 'N':
                # 메인화면으로 이동
                print('등록을 취소합니다.')
                break
            else:
                print('PLEASE CHOICE Y, N !!!')
                continue
#############검색파트############################################################################################
    elif user_pick.upper() == 'S':
        while user_pick.upper() != 'Y' or user_pick.upper() != 'N':
            print('='*30)
            print('회원 정보 검색')
            print('-'*30)
            while True:  # 테이블을 정의한 대로 이름과 전화번호를 필수로 받아 복합키로 설정하기위한 반복문
                name = input('검색할 회원정보의 이름 : ')
                if(name == ''):
                    continue
                else:
                    break
            while True:
                phone = input('이름과 함께 등록된 전화번호 : ')
                if(phone == ''):
                    continue
                else:
                    break
            print('='*30)
            user_pick = input('검색(Y) / 메인화면(N) : ')
            if user_pick.upper() == 'Y':
                result = func_DML.select(name, phone)
                # 입력된 데이터를 테이블에서 조회하는 구문
                try:
                    print('='*30)
                    print('검색 결과')
                    print('-'*30)
                    print('이    름 : ', result[0][0])  # 리스트의 요소를 가져오는 방법
                    print('나    이 : ', result[0][1])
                    print('전화번호 : ', result[0][2])
                    print('이 메 일 : ', result[0][3])
                    print('='*30)
                except IndexError:  # 조회했을때 없을 경우, 예외처리
                    print(' ▶ 검색한 회원정보 결과가 없습니다.')
                    print('검색화면으로 돌아갑니다.\n')
                    continue
                else:
                    print(' ▶ 회원정보 검색이 완료되었습니다.\n')
                    user_pick = input('다시 검색(Y) / 메인화면(N)  입력 : ')
                    if user_pick.upper() == 'Y':
                        continue
                    elif user_pick.upper() == 'N':
                        break
                    else:
                        print('PLEASE CHOICE Y, N !!!')
                        continue
            elif user_pick.upper() == 'N':
                print('검색을 취소합니다\n')
                break
            else:
                print('PLEASE CHOICE Y, N !!!')
                continue
#############수정파트############################################################################################
    elif user_pick.upper() == 'U':
        while user_pick.upper() != 'Y' or user_pick.upper() != 'N':
            print('='*30)
            print('회원 정보 수정')
            print('-'*30)
            while True:  # 테이블을 정의한 대로 이름과 전화번호를 필수로 받아 복합키로 설정하기위한 반복문
                check_name = input('수정할 회원정보의 이름 : ')
                if(check_name == ''):
                    continue
                else:
                    break
            while True:
                check_phone = input('이름과 함께 등록한 전화번호 : ')
                if(check_phone == ''):
                    continue
                else:
                    break
            user_pick = input('입력한 회원의 정보 수정(Y) / 취소 후 메인화면(N) : ')
            print('-'*30)
            # 입력을 하지 않고 건너뛰면 원래 있던 정보를 유지하며 입력된 값만 바꿔 갱신하는 구문
            if (user_pick.upper() == 'Y'):
                update_obj = func_DML.select(check_name, check_phone)
                # 줄바꿈을 하지 않고 input()함수를 받기 위한 줄바꿈 제거
                print('이    름: {} ▶ : '.format(update_obj[0][0]), end='')
                new_name = input()
                if(new_name == ''):
                    new_name = update_obj[0][0]
                print('나    이: {} ▶ : '.format(update_obj[0][1]), end='')
                new_age = input()
                if(new_age == ''):
                    new_age = update_obj[0][1]
                print('전화번호: {} ▶ : '.format(update_obj[0][2]), end='')
                new_phone = input()
                if(new_phone == ''):
                    new_phone = update_obj[0][2]
                print('이 메 일: {0} ▶ : '.format(update_obj[0][3]), end='')
                new_email = input()
                if(new_email == ''):
                    new_email = update_obj[0][3]
                user_pick = input('회원 정보를 수정하시겠습니까? 예(Y) / 아니오(N) : ')
                while user_pick.upper() != 'Y' or user_pick.upper() != 'N':
                    if user_pick.upper() == 'Y':
                        func_DML.update(new_name, new_age, new_phone,
                                        new_email, check_name, check_phone)
                        break
                    elif user_pick.upper() == 'N':
                        print('회원정보수정을 취소하고 메인화면으로 돌아갑니다.')
                        break
                    else:
                        print('PLEASE CHOICE Y, N !!!')
                        continue
                print(' ▶ 회원 정보 수정을 완료하였습니다.')
                break
            elif user_pick.upper() == 'N':
                print('회원정보수정을 취소하고 메인화면으로 돌아갑니다.')
                break
            else:
                print('PLEASE CHOICE Y, N !!!')
                continue
#############삭제파트############################################################################################
    elif user_pick.upper() == 'D':
        print('='*30)
        print('회원 정보 삭제')
        print('-'*30)

        while True:  # 테이블을 정의한 대로 이름과 전화번호를 필수로 받아 복합키로 설정하기위한 반복문
            name = input('삭제할 회원정보의 이름 :')
            if(name == ''):
                continue
            else:
                break
        while True:
            phone = input('이름과 함께 등록된 전화번호 : ')
            if(phone == ''):
                continue
            else:
                break
        print('='*30)
        while user_pick.upper() != 'Y' or user_pick.upper() != 'N':
            user_pick = input('삭제(Y) / 취소(N) 입력 :')
            # 입력한 값과 일치하는 로우가 있으면 삭제하는 구문, 테이블이 없더라도 삭제함(ㅋ)
            if user_pick.upper() == 'Y':
                print('회원정보를 삭제합니다...')
                result = func_DML.delete(name, phone)
                if result == 1:
                    print('입력하신 회원정보 삭제가 완료되었습니다.\n')
                    break
                else:
                    print('삭제할 회원정보가 존재하지 않습니다.')
                    break
            elif user_pick.upper() == 'N':
                print('회원정보 삭제를 취소합니다\n')
                break
            else:
                print('PLEASE CHOICE Y, N !!!')
                continue

    else:
        print('PLEASE CHOICE Q, I, S, D, U !!!\n')
