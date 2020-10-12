import pymssql
conn = pymssql.connect(server='127.0.0.1:1433', user='wuusDB', password='*****', database='pythonDB', charset='utf8')
cursor = conn.cursor()

# 修改、刪除
id = input("id：")
name = input("name：")
sql = "SELECT * FROM scores WHERE id={} AND name='{}'".format(id, name)
print(sql)
cursor.execute(sql)
row = cursor.fetchone()
print(row)

if row != None:
    id, name, chinese, english, math = row
    choice = input("1.修改   2.刪除   0.結束：")
    if choice == '1':
        print("修改...")
        temp = input("[" + name + "]" + "修改名字為：")
        if temp != '':
            name = temp
        temp = input("[" + str(chinese) + "]" + "修改中文成績為：")
        if temp != '':
            chinese = temp
        temp = input("[" + str(english) + "]" + "修改英文成績為：")
        if temp != '':
            english = temp
        temp = input("[" + str(math) + "]" + "修改數學成績為：")
        if temp != '':
            math = temp
        sql = "UPDATE scores SET name='{}',chinese={},english={},math={} WHERE id={}".format(name, chinese, english, math, id)
        print(sql)
        cursor.execute(sql)
        conn.commit()
    elif choice == '2':
        sql = "DELETE FROM scores WHERE id={}".format(id)
        cursor.execute(sql)
        conn.commit()
        print("資料已刪除")
    else:
        # choice == '0'
        print("程式結束")

conn.close()
