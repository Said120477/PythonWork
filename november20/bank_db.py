import sqlite3

connection = sqlite3.connect('C:\\Users\\User\\Documents\\уроки PY\\todo')
cursor = connection.cursor()

cursor.execute('select * from bank')
cursor.execute('update bank set money = money + 500 where name = "миша"')

connection.commit()

cursor.execute('update bank set money = money - 500 where name = "антон"')
print(cursor.fetchall())
connection.commit()




connection.close()