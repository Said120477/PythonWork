
import  json
from sqlalchemy import create_engine, text
import telebot
from telebot import types
import random

class TaskModel:

    def __init__(self, filename):
        self.filename = filename
        self.tasks = self._load_from_file()

    def get_tasks(self):
        return self.tasks

    def add_tasks(self, task):
        self.tasks.append(task)

        self._save_to_file()


    def _load_from_file(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            tasks = json.load(f)
        return tasks

    def _save_to_file(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f)


class NoteModelSQL:
    def __init__(self, db_name):
        self.db_name = db_name


    def get_tasks(self, user_id):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = self._dict_factory
        cursor = connection.cursor()
        rows = cursor.execute('select * from task where user_id = ?', (user_id, )).fetchall()
        connection.close()
        return rows

    def add_task(self, text, user_id):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = self._dict_factory
        cursor = connection.cursor()
        rows = cursor.execute('insert into task (name, user_id) values (?, ?)', (text, user_id))
        connection.commit()
        connection.close()
        return rows


    def get_user(self, telegram_id):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = self._dict_factory
        cursor = connection.cursor()
        rows = cursor.execute('select * from user where telegram_id = ?', (telegram_id, )).fetchone()
        connection.close()
        return rows

    def add_user(self, telegram_id):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = self._dict_factory
        cursor = connection.cursor()
        cursor.execute('insert into user (telegram_id) values (?)', (telegram_id, )).fetchone()
        connection.commit()
        connection.close()


    @staticmethod
    def _dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

token = '7992348444:AAF8Gc-OWI_bkiYLF8rHvBHjjznUSrJ6izw'
bot = telebot.TeleBot(token)

user_state = ''
ADD_STATE = 'add'
db_name = 'C:\\Users\\User\\Documents\\уроки PY\\PythonWork\\db\\bot_todo'
#db = TaskModel('tasks.json')
db = NoteModelSQL(db_name)



@bot.message_handler(commands=['weather'])  # декоратор
def weather(message):
    print(message)
    bot.reply_to(message, text='погода не очень, уже зима')

@bot.message_handler(commands=['keyboard'])
def keyboard(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('добавить задачу')
    markup.add(button)
    bot.send_message(message.chat.id, 'какой то текст', reply_markup=markup)


@bot.message_handler(commands=['coin'])  # декоратор
def coin(message):
    res = random.choice(['орёл', 'решка'])
    print(message)
    bot.reply_to(message, res)

@bot.message_handler(commands=['start'])  # декоратор
def start(message):
    description = 'Я бот для создания списка дел. Жми кнопку или команду /add для добавления'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('добавить задачу')
    button2 = types.KeyboardButton('просмотреть все задачи')
    markup.add(button)
    markup.add(button2)

    telegram_id = message.chat.id
    user = db.get_user(telegram_id)
    print(telegram_id, user)
    if not user:
        db.add_user(telegram_id)
        bot.reply_to(message, 'я вас добавил')
    bot.send_message(message.chat.id, description, reply_markup=markup)


@bot.message_handler(regexp='добавить задачу')
@bot.message_handler(commands=['add'])  # декоратор
def add(message):
    global user_state
    user_state = 'add'
    print(message)
    bot.reply_to(message, text='введи текст задачи: ')
    
@bot.message_handler(regexp='просмотреть все задачи')
@bot.message_handler(commands=['tasks'])  # декоратор
def get_task_list(message):
    telegram_id = message.chat.id
    user = db.get_user(telegram_id)
    if not user:
        return bot.reply_to(message, 'вас нет в базе')
    #print(user)
    tasks = db.get_tasks(user['id'])
    if not tasks:
        return bot.reply_to(message, 'у вас нет задач')
    tasks = db.get_tasks(user['id'])
    tasks = [task['name'] for task in tasks]
    tasks_string = '\n'.join(tasks)
    bot.reply_to(message, tasks_string)

@bot.message_handler(commands=['end'])  # декоратор
def end_state(message):
    global user_state
    user_state = ''
    bot.reply_to(message,'мы вышли из сеанса добавления в базу')

@bot.message_handler(func=lambda message: True)  # декоратор
def get_task(message):
    global user_state
    telegram_id = message.chat.id
    user = db.get_user(telegram_id)

    if user_state == ADD_STATE:
        db.add_task(message.text, user['id'])
        user_state = ''
        print(db.get_tasks(user['id']))
        bot.reply_to(message, text='добавил в базу ')



bot.infinity_polling()