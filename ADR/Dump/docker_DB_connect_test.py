from datetime import datetime
from time import sleep

import MySQLdb
import mariadb
import pymysql


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}', flush=True)  # Press Ctrl+F8 to toggle the breakpoint.


def test_DB():
    args_list = []

    for host in ['localhost', '127.0.0.1', 'mariaDB']:
        for user in ['root', 'user']:
            for port in [3306, 4491]:
                args_list.append({
                    'host': host,
                    'user': user,
                    'port': port,
                })

    for args in args_list:
        print(args)
        try:
            # 커서 생성
            conn = mariadb.connect(
                host=args['host'],
                user=args['user'],
                password='1234',
                db='students',
                port=args['port']
            )
            print("성공", flush=True)
        except Exception as e:
            print(e, flush=True)

        try:
            # 커서 생성
            conn = pymysql.connect(
                host=args['host'],
                user=args['user'],
                password='1234',
                db='students',
                port=args['port']
            )
            print("성공", flush=True)
        except Exception as e:
            print(e, flush=True)
        try:
            # 커서 생성
            conn = MySQLdb.connect(
                host=args['host'],
                user=args['user'],
                password='1234',
                db='students',
                port=args['port']
            )
            print("성공", flush=True)
        except Exception as e:
            print(e, flush=True)
        print("-------------------------------")


def run_DB_local():
    try:
        # 커서 생성
        conn = mariadb.connect(
            host='localhost',
            user='user',
            password='1234',
            db='students',
            port=4491
        )
        print("성공", flush=True)
    except Exception as e:
        print(e)

def run_DB_docker():
    try:
        # 커서 생성
        conn = mariadb.connect(
            host='mariaDB',
            user='user',
            password='1234',
            db='students',
            port=3306
        )
        print("성공", flush=True)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    while True:
        print_hi(f'PyCharm{datetime.now()}')
        sleep(1)
        # test_DB()
        # run_DB_local()
        run_DB_docker()
