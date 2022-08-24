import pymysql
import mafia.mafiavo as vo

class mafiaDao :
    def connect(self):
        return pymysql.connect(host='localhost', user='root', password='root', db='mafia', charset='utf8')


    def insert(self, m):
        conn = self.connect()
        cursor = conn.cursor()
        sql = 'insert into member values(%s, %s, %s, %s)'
        d = (m.id, m.pwd, 0, 0)
        cursor.execute(sql, d)
        conn.commit()
        conn.close()

    def select(self, id):
        conn = self.connect()
        sql = 'select * from member where id=%s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql, id)  # sql실행. 실행한 결과는 cursor 객체에 담아
        row = cursor.fetchone()#검색 결과 한줄추출
        conn.close()
        if row != None:
            return vo.mafiavo(row[0], row[1], row[2], row[3])

    def update(self, id, pwd, win, lose):# 수정할 제품번호와 새 가격을 Test 객체로 받아옴
        conn = self.connect()
        sql = 'update member set win=%s, lose=%s where id=%s, pwd=%s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        d = (win, lose, id, pwd)
        cursor.execute(sql, d)
        conn.commit()  # 쓰기 완료
        conn.close()

    def delete(self, id):
        conn = self.connect()
        sql = 'delete from member where id=%s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        # d = (name, ip)
        cursor.execute(sql, id)
        conn.commit()  # 쓰기 완료
        conn.close()

    def test():

    def test2():

