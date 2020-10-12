def menu():
    print("<帳號、密碼管理系統>")
    print('--------------------------------')
    print('1. 新增帳號、密碼')
    print('2. 顯示帳號、密碼')
    print('3. 修　改　密　碼')
    print('4. 刪除帳號、密碼')
    print('0. 結　束　程　式')
    print('--------------------------------')


def input_data():
    while True:
        name = input('請輸入帳號(按 Enter 結束)：')
        if name == '':
            break

        cursor = conn.execute("SELECT * FROM number WHERE name='{}'".format(name))
        row = cursor.fetchone()
        # print(row)
        if row != None:
            print('帳號已存在!')
            continue

        password = input('請輸入密碼：')
        sql1 = "INSERT INTO number(name, password) VALUES('{}', {});".format(name, password)    # '{}'字串資料
        cursor.execute(sql1)
        conn.commit()
        break


def disp_data():
    sql2 = "SELECT * FROM number"
    cursor = conn.execute(sql2)
    rows = cursor.fetchall()

    print("帳號\t密碼")
    for row in rows:
        print('{}\t\t{}'.format(row[0], row[1]))


def edit_data():
    while True:
        name = input("請輸入要修改的帳號(按 Enter 結束)：")
        if name == '':
            break

        cursor = conn.execute("SELECT * FROM number WHERE name='{}'".format(name))
        row = cursor.fetchone()
        # print(row)
        if row == None:
            print('帳號未存在!')
            continue

        password = input("請輸入新密碼：")
        sql3 = f"UPDATE number SET password ='{password}' WHERE name = '{name}' "
        cursor.execute(sql3)
        print('密碼已更新完成!')
        conn.commit()
        break


def delete_data():
    while True:
        name = input("請輸入要刪除的帳號(按 Enter 結束)：")
        if name == '':
            break

        cursor = conn.execute("SELECT * FROM number WHERE name='{}'".format(name))
        row = cursor.fetchone()
        # print(row)
        if row == None:
            print('帳號未存在!')
            continue

        yesno = input("確認(Y/N)刪除" + name + "帳號嗎?").upper()
        if yesno == 'Y':
            sql4 = f"DELETE FROM number WHERE name = '{name}' "
            cursor.execute(sql4)
            print('帳號已刪除!')
            conn.commit()
        else:
            print("帳號未刪除!")
        break


### 主程式從這裡開始 ###
import sqlite3

conn = sqlite3.connect('account.db')
cursor = conn.cursor()

sql = '''CREATE TABLE IF NOT EXISTS number(
    'name' TEXT PRIMARY KEY NOT NULL,
    'password' INTEGER NOT NULL)'''
cursor.execute(sql)


while True:
    menu()
    choice = int(input('請輸入您的選擇：'))
    print()
    if choice == 1:
        input_data()
    elif choice == 2:
        disp_data()
    elif choice == 3:
        edit_data()
    elif choice == 4:
        delete_data()
    elif choice == 0:
        break
    else:
        print('未有該功能選項，請重新輸入。\n')
        continue

conn.close()
print('程式執行完畢！')
