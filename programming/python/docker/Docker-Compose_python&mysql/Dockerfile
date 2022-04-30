FROM python
# 파이썬 이미지를 사용
COPY . .
# 현재 존재하는 파일들을 파이썬 이미지를 실행할 컨테이너의 루트 디렉토리에 복사
RUN pip install pymysql && pip install cryptography
# pysql:파이썬으로 mysql에 연결하고, cryptography:대칭키를 이용하여 암호화 및 복호화
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /
# mysql 컨테이너가 실행된 후에, python의 컨테이너를 depends on하여 실행할때, 
# 데이터베이스 파일들이 만들어지는동안 지연을 시켜주기 위해 쉘스크립트를 루트 디렉토리에 다운받는 명령어
RUN chmod +x /wait-for-it.sh
# 위에서 지연시키는 파일을 실행권한을 부여하고 실행하기 위함 => 실행은 docker-compose.yaml파일에 정의된 명령을 실행

# 빌드 docker build -t [image name] .
# 컨테이너에서 파이썬파일 실행(docker-compose) docker compose run python
