

class Tasksmodel:
    def __init__(self):
        self.tasks = [{'name': 'поспать', 'status': 'в ожидании'}]

    def get_tasks(self):
        return self.tasks

    def add_task(self, name):
        task = {'name': name, 'status': 'в ожидании'}
        self.tasks.append(task)

    def complete_task(self, task_number):
        self.tasks[task_number]['status'] = 'выполнено'

    def remove_task(self, number):

    

class View:
    @staticmethod
    def show_all_tasks(tasks):
        for number, task in enumerate(tasks, 1):
            print(f'{number}. {task['name']}: {task['status']}')

    @staticmethod
    def show_add_task():
        return input('введи название задачи: ')

    @staticmethod
    def show_complete_task():
        return int(input('введи номер задачи: '))
    @staticmethod
    def show_remove_task():
        return input('введи название удаленной задачи: ')
class Controller:
    '''класс для бизнес-логики. взаимодействует с моделью и представлением'''
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def add_task(self):
        '''добавление задачи'''
        tasks = self.model.get_tasks()
        self.view.show_all_tasks(tasks)
        task_name = self.view.show_add_task()
        self.model.add_task(task_name)
        self.view.show_all_tasks(tasks)

    def show_tasks(self):
        tasks = self.model.get_tasks()
        self.view.show_all_tasks(tasks)

    def complete_task(self):
        task_number = self.view.show_complete_task()
        task_number -= 1
        self.model.complete_task(task_number)

    def remove_task(self, task):
        number = input('номер')
        self.model.remove_task(number)
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Задача '{task}' удалена!")
        else:
            print(f"Задача '{task}' не найдена в списке!")


model = Tasksmodel()
view = View()
contr = Controller(view, model)


while True:
    print('1- добавить задачу')
    print('2- выполнить задачу')
    print('3- посмотреть список задач')
    print('4- удалить задачу из списка')
    print('5- выйти')

    choice = input('что ты хочешь сделать: ')

    if choice == '1':
        contr.add_task()

    elif choice == '2':
        contr.complete_task()

    elif choice == '3':
        print('вот ваши задачи: ')
        contr.show_tasks()

    elif choice == '4':
        contr.remove_task()

    elif choice == '5':
        break