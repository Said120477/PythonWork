tasks = [{'name': 'поспать', 'status': 'в ожидании'}]

def add_task(name):
    task = {'name': name, 'status': 'в ожидании'}
    tasks.append(task)
def complete_task(task_number):
    '''выполнение задачи'''
    if len(tasks) >= task_number:
        task = tasks[task_number]
        task['status'] = 'выполнена'


def show_task():
    for number, task in enumerate(tasks, 1):
        print(f'{number}. {task['name']}: {task['status']}')

while True:
    print('1- добавить задачу')
    print('2- выполнить задачу')
    print('3- посмотреть список задач')
    print('4- выйти')


    choice = input('что ты хочешь сделать: ')

    if choice == '1':
        show_task()
        name = input('название задачи: ')
        add_task(name)
        show_task()

    elif choice == '2':
        show_task()
        task_number = int(input('введи номер задачи: '))
        task_number -= 1
        complete_task(task_number)
        show_task()

    elif choice == '3':
        show_task()

    elif choice == '4':
        break