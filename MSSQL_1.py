"""
python 連線 mssql
(2) INSERT INTO
(3) SELECT
"""

import pymssql

conn = pymssql.connect(server='127.0.0.1:1433', user='*****', password='*****', database='pythonDB', charset='utf8')
cursor = conn.cursor()

# ----------------------------------------------------------------
while True:
    name = input("請輸入姓名(Enter 結束)：")
    if name == '':
        break
    else:
        chinese = int(input("請輸入中文成績："))
        english = int(input("請輸入英文成績："))
        math = int(input("請輸入數學成績："))

        sql = "INSERT INTO scores(name, chinese, english, math) VALUES('{}', {}, {}, {})".format(name, chinese, english, math)
        cursor.execute(sql)
        conn.commit()

        sql = "SELECT * FROM scores"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print('--------------------')

conn.close()

# ----------------------------------------------------------
import pymssql

conn = pymssql.connect(server='127.0.0.1:1433', user='*****', password='*****', database='pythondb', charset='utf8')


with conn.cursor() as cursor:   # 建立cursor物件
    id = input("請輸入查詢的id( Enter 結束)：")
    name = input("請輸入名字：")
    sql = "SELECT * FROM scores WHERE id={} AND name='{}'".format(id, name)     # '{}' 字串--> SQL只接受單引號
    cursor.execute(sql)
    row = cursor.fetchone()
    print(row)

conn.close()