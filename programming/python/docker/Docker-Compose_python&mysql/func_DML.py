import pymysql


# 테이블에 존재하는 행의 개수를 세어오는 함수
def memlist_information() -> int:
    with pymysql.connect(
        host="db",
        port=3306,
        user="root",
        password="t123456789",
        db="memlist",
        charset="utf8"
    ) as db_conn:
        with db_conn.cursor() as cursor:
            count_query = "SELECT * FROM meminfo"
            cursor.execute(count_query)
            db_conn.commit()
            mem_number = len(list(cursor))
    return mem_number


# 테이블 조회하는 함수
# 매개변수는 이름과 전화번호
def select(ins_name, ins_phone) -> tuple:
    trans_ins_phone = ins_phone.replace('-', '')
    with pymysql.connect(
        host="db",
        port=3306,
        user="root",
        password="t123456789",
        db="memlist",
        charset="utf8"
    ) as db_conn:
        with db_conn.cursor() as cursor:
            select_query = "SELECT name, age, phone, email FROM meminfo WHERE name ='{}' AND phone='{}' ".format(
                ins_name, trans_ins_phone)
            cursor.execute(select_query)
            db_conn.commit()
            return cursor.fetchall()


# 데이터 삽입하는 함수
# 매개변수는 이름, 나이, 전화번호, 이메일
def insert(ins_name, ins_age, ins_phone, ins_email):
    # 번호를 입력할 때, 010-3414-8320 or 01034148320 '-'을 입력하나, 하지 않나 동일하게 저장하기 위함
    trans_ins_phone = ins_phone.replace('-', '')
    with pymysql.connect(
        host="db",
        port=3306,
        user="root",
        password="t123456789",
        db="memlist",
        charset="utf8"
    ) as db_conn:
        with db_conn.cursor() as cursor:
            insert_query = "INSERT INTO meminfo(name, age, phone, email) VALUE ('{}', '{}', '{}', '{}')".format(
                ins_name, ins_age, trans_ins_phone, ins_email)
            cursor.execute(insert_query)
            db_conn.commit()


# 데이터 갱신하는 함수
# 사용자의 정보(이름과 전화번호)를 통해 일치하는 행의 정보를 갱신
def update(new_name, new_age, new_phone, new_email, ins_name, ins_phone):
    trans_new_phone = new_phone.replace('-', '')
    trans_ins_phone = ins_phone.replace('-', '')
    with pymysql.connect(
        host="db",
        port=3306,
        user="root",
        password="t123456789",
        db="memlist",
        charset="utf8"
    ) as db_conn:
        with db_conn.cursor() as cursor:
            update_query = "UPDATE meminfo SET name='{}', age='{}', phone='{}', email='{}' WHERE name='{}' AND phone='{}'".format(
                new_name, new_age, trans_new_phone, new_email, ins_name, trans_ins_phone)
            cursor.execute(update_query)
            db_conn.commit()


# 데이터 삭제하는 함수
# 매개변수 이름과 전화번호를 입력하고 동일한 행을 삭제
def delete(ins_name, ins_phone):
    trans_ins_phone = ins_phone.replace('-', '')
    with pymysql.connect(
        host="db",
        port=3306,
        user="root",
        password="t123456789",
        db="memlist",
        charset="utf8"
    ) as db_conn:
        with db_conn.cursor() as cursor:
            delete_query = "DELETE FROM meminfo WHERE name ='{}' AND phone='{}' ".format(
                ins_name, trans_ins_phone)
            cursor.execute(delete_query)
            db_conn.commit()
            # delete_query을 실행한 후의 결과값(삭제된 행의 개수)
            # rowcount(패치후 로우의 수를 가져오는 시스템 함수)를 이용해 값을 반환
            return cursor.rowcount
