# db1.py
import sqlite3

#파일에 저장
con = sqlite3.connect("c:\\work\\sample.db")
#구문 실행은 커서객체에서
cur = con.cursor()
#테이블 구조 생성(ANSI SQL 82, 99에서 표준)
cur.execute("create table if not exists PhoneBook " + 
            "( id integer primary key autoincrement, name text, phoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook (name, phoneNum) values ('홍길동', '010-123');")

#입력 파라미터 처리
name = "이다빈"
phoneNumber = "010-232"
cur.execute("insert into PhoneBook (name, phoneNum) values (?, ?);", (name, phoneNumber))

#다중의 레코드 입력
datalist = ("이연복","010-259"),("이유빈","010-951")
cur.executemany("insert into PhoneBook (name, phoneNum) values (?, ?);", datalist)

#결과 확인
cur.execute("select * from PhoneBook;")

print(cur.fetchall())

#커밋을 실행(자동 아님)
con.commit()

#연결닫기
con.close()
