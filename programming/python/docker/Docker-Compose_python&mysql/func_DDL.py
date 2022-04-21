import pymysql


# mysql에 연결한 뒤에, 테이블을 생성하는 쿼리
def create_table_meminfo():
    with pymysql.connect(
        host="db",
        port=3306,
        user="root",
        password="t123456789",
        db="memlist",
        charset="utf8",
    ) as db_conn:
        with db_conn.cursor() as cursor:
            create_table_query = """ CREATE TABLE IF NOT EXISTS meminfo(
                         name VARCHAR(50) NOT NULL,
                         age INT,
                         phone VARCHAR(100) NOT NULL,
                         email VARCHAR(100),             
                        PRIMARY KEY(name, phone)); """
            cursor.execute(create_table_query)
            db_conn.commit()
