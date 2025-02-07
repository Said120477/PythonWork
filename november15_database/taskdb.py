import sqlite3

db = 'C:\\Users\\User\\Documents\\уроки PY\\todo'

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)

    def get_tasks(self, user_id):
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('select * from task where user_id = ?', (user_id, ))
            rows = cursor.fetchall()
            return rows

    def get_task_by_id(self, user_id, task_id):
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute('select * from task where user_id = ? and task_id = ?', (user_id, task_id))
            row = cursor.fetchone()
            return row


    def add_tasks(self, name, user_id):
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('insert into task (name, status, user_id ) values (?, ?, ?)', (name, 'сделать', user_id))

    def delete_tasks(self, task_id, user_id):
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('delete from task where user_id = ? and id = ?', (task_id, user_id))
            print('задача удалена!')

    def update_tasks(self, task_id):
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute("update task set status = 'сделано' where id = ?", (task_id, ))

    def get_user(self, login, password):
        with self.connection as connection:
            cursor = connection.cursor()
            rows = cursor.execute("select * from users where name = ? and password = ?", (login, password))
            res = rows.fetchone()
            return res
    def __del__(self):
        print('заканчиваю работу с базой')
        self.connection.close()

emoji = {'сделать': '🔵', 'сделано': '🟢'}


class User:
    def __init__(self, name: str, password: str, db: Database):
        self.name = name
        self.password = password
        self.db = db

    def auth(self):
        user = self.db.get_user(name, password)
        if user:
            return user[0]
        return None


db = Database('C:\\Users\\User\\Documents\\уроки PY\\todo')

name = input('введи имя: ')
password = input('введи пароль: ')

auth = False

user_id = User(name, password, db).auth()

if user_id:
    auth = True
    print('авторизация прошла успешно!')
else:
    print('неверные пароль или логин!')




while True and auth:
    print('что хотите сделать?')
    print('1 - прочитать задачи')
    print('2 - добавить задачу')
    print('3 - Удалить задачу')
    print('4 - выполнить задачу')

    res = input('Введи номер: ')
    if res == '1':
        rows = db.get_tasks(user_id)
        print('\nВот список задач: ')
        for row in rows:
            task_string = f'{row[0]} {row[1]} {row[2]}{emoji[row[2]]}'
            print(task_string)
        print('\n')

    if res == '2':
        name = input('Введи задачу: ')
        db.add_tasks(name, user_id)
        print('Задача добавлена')

    if res == '3':
        task_id = input('Введи id задачи: ')
        task = db.get_task_by_id(user_id, task_id)
        if task:
            db.delete_tasks(task_id, user_id)
            print('Задача удалена')
        else:
            print('такой задачи нет')


    if res == '4':
        task_id = input('Введи id задачи: ')
        db.update_tasks(task_id)
        print('задача выполнена')

    if res == 'q':
        break















