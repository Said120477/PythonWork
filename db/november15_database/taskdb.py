import sqlite3

def get_tasks():
    connection = sqlite3.connect('C:\\Users\\User\\Documents\\уроки PY\\todo')
    cursor = connection.cursor()
    cursor.execute('select * from task')
    rows = cursor.fetchall()
    connection.close()
    return rows

def add_tasks(name):
    connection = sqlite3.connect('C:\\Users\\User\\Documents\\уроки PY\\todo')
    cursor = connection.cursor()
    cursor.execute('insert into task (name, status ) values (?, ?)', (name, 'сделать'))
    connection.commit()
    connection.close()

def delete_tasks(task_id):
    connection = sqlite3.connect('C:\\Users\\User\\Documents\\уроки PY\\todo')
    cursor = connection.cursor()
    cursor.execute('delete from task where id = ?', (task_id, ))
    connection.commit()
    connection.close()

def update_tasks(task_id):
    connection = sqlite3.connect('C:\\Users\\User\\Documents\\уроки PY\\todo')
    cursor = connection.cursor()
    cursor.execute("update task set status = 'сделано' where id = ?", (task_id, ))
    connection.commit()
    connection.close()

emoji = {'сделать': '🔵', 'сделано': '🟢'}



while True:
    print('что хотите сделать?')
    print('1 - прочитать задачи')
    print('2 - добавить задачу')
    print('3 - Удалить задачу')
    print('4 - выполнить задачу')

    res = input('Введи номер: ')
    if res == '1':
        rows = get_tasks()
        print('\nВот список задач: ')
        for row in rows:
            task_string = f'{row[0]} {row[1]} {row[2]}{emoji[row[2]]}'
            print(task_string)
        print('\n')

    if res == '2':
        name = input('Введи задачу: ')
        add_tasks(name)
        print('Задача добавлена')

    if res == '3':
        task_id = input('Введи id задачи: ')
        delete_tasks(task_id)
        print('Задача удалена')

    if res == '4':
        task_id = input('Введи id задачи: ')
        update_tasks(task_id)
        print('задача выполнена')

    if res == 'q':
        break















