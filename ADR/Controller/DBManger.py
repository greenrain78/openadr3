from logging import getLogger

import pymysql

from settings import mariaDB_IP, mariaDB_ID, mariaDB_password, mariaDB_DB_name, mariaDB_port

log = getLogger(__name__)


def getConn():
    # 커서 생성
    conn = pymysql.connect(
        host=mariaDB_IP,
        user=mariaDB_ID,
        password=mariaDB_password,
        db=mariaDB_DB_name,
        charset='utf8',
        port=mariaDB_port
    )
    return conn


def runSQL(sql):
    try:
        conn = getConn()
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
        log.error(e)
