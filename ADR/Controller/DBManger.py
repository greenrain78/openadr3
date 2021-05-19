import pymysql


class DBSession:

    @classmethod
    def getSQL(cls, sql):
        print("run getSQL")
        try:
            # 커서 생성
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='root!',
                db='departments',
                charset='utf8',
                port=4491
            )
            assert conn == True

            # 커서 생성
            cur = conn.cursor()
            # sql문 실행
            cur.execute(sql)
            result = cur.fetchall()

            # DB에 반영
            conn.commit()
            conn.close()
            return result
        except Exception as e:
            print(e)
