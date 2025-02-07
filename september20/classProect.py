from september13.practic import Programmer
class Project:
    def __init__(self, name):
        self.name = name
        self.programmers = []

    def assign_programmer(self, programmer):
        self.programmers.append(programmer)
        print(f'добавил {programmer.name}')

    def add_hours(self, hours):
        for programmer in self.programmers:
            programmer.hours_to_do += hours

    def get_salary(self):
        '''считаем сумму всех затрат на проект'''
        all_salary = 0
        for programmer in self.programmers:
            salary = programmer.hours_to_do * programmer.salary
            all_salary += salary
        return  all_salary

project = Project(name='Сайт')
programmer1 = Programmer('Васильев Джек', 'Junior')
programmer2 = Programmer('Васильев Иван', 'Middle')
programmer3 = Programmer('Васильев Том', 'Senior')

project.assign_programmer(programmer1)
project.assign_programmer(programmer2)
project.assign_programmer(programmer3)

print(programmer1.hours_to_do)
print(programmer2.hours_to_do)
print(programmer3.hours_to_do)
project.add_hours(10)
print('денег потребуется', project.get_salary())


