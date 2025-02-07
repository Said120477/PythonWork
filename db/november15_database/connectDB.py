import sqlite3

connection = sqlite3.connect('C:\\Users\\User\\Documents\\уроки PY\\st')
cursor = connection.cursor()

cursor.execute('select * from student')
rows = cursor.fetchall()
# print(rows)
# for row in rows:
#     print(f'{row[1], row[2]}')
student = ['коля', 'asd@sdf.ru', '2']
cursor.execute("insert into student (fio, email, class_id) values (?, ?, ?);", (student[0], student[1], student[2]))
cursor.execute("insert into student (fio, email, class_id) values ('Ежик', 'dsf', 1)")
connection.commit()


cursor.close()
connection.close()

