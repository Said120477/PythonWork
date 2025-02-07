# Задание 2
# Рассмотрим объект «Программист», который задаётся именем, должностью и
# количеством отработанных часов. Каждая должность имеет собственный оклад
# (заработную плату за час работы). В нашей импровизированной компании
# существуют 3 должности:
# ● Junior — с окладом 10 тугриков в час;
# ● Middle — с окладом 15 тугриков в час;
# ● Senior — с окладом 20 тугриков в час по умолчанию и +1 тугрик за
# каждое новое повышение.
# Напишите класс Programmer, который инициализируется именем и
# должностью (отработка у нового работника равна нулю). Класс реализует
# следующие методы:
# ● work(time) — отмечает новую отработку в количестве часов time;
# ● rise() — повышает программиста;
# ● info() — возвращает строку для бухгалтерии в формате: <имя>
# <количество отработанных часов>ч. <накопленная зарплата>тгр.

class Programmer:
    SALARY_INFO = {'Junior': 10, 'Middle': 15, 'Senior': 20}
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

        self.all_salary = 0
        self.all_time = 0

        self.extra_salary = 0
        self.hours_to_do = 0
        self.salary = self.SALARY_INFO[self.grade]

    def work(self, time):
        self.all_time += time
        salary = self.salary * time
        self.all_salary += salary
        print(f'отработал {time}ч')
        self._check_bonus()

    def rise(self):
        if self.grade == 'Junior':
            self.grade = 'Middle'
            self.salary = self.SALARY_INFO[self.grade]

        elif self.grade == 'Middle':
            self.grade = 'Senior'
            self.salary = self.SALARY_INFO[self.grade]

        elif self.grade == 'Senior':
            self.salary += 1



    def info(self):
        print((f'{self.name} {self.all_time}ч {self.all_salary} тугрик'))

    def _check_bonus(self):
        if self.all_time >= 1000:
            self.all_salary += 10000





