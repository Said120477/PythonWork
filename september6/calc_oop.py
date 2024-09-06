class Calculator:

    def __init__(self, number_1, number_2): #конструктор,который выполняется при создании обьекта
        self.number_1 = number_1
        self.number_2 = number_2

    def add(self):
        return self.number_1 + self.number_2

    def subtract(self):
        return self.number_1, self.number_2

    def division(self):
        if number_2 != 0:
            return self.number_1 / self.number_2

    def multiply(self):
        return self.number_1 * self.number_2


class Logger:
    def __init__(self, filename):
        self.filename = filename
    def log_to_file(self, number_1, number_2, action):
        with open(self.filename, 'a', encoding='utf-8') as f:
            log_string = f"{number_1} {number_2}: {action} \n"
            f.write(log_string)
    def read_logs(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            print(f.read())





print('введи два числа ')
number_1 = int(input('первое число: '))
number_2 = int(input('второе число: '))

print('1 - сложить')
print('2 - вычесть')
print('3 - прочитать логи')
print('4 - деление')
print('5 - умножение')

ans = input('выбери операцию: ')

#создали экземпляры нужных классов
calculator = Calculator(number_1, number_2)
logger = Logger('logs.txt')
logger_new = Logger('logs_new.txt')

if ans == '1':
    res = calculator.add()
    print(res)
    logger.log_to_file(number_1, number_2, action='сложение')
elif ans == '2':
    res = calculator.subtract()
    print(res)
    logger.log_to_file(number_1, number_2, action='вычитание')
elif ans == '3':
    logger.read_logs()
elif ans == '4':
    res = calculator.division()
    print(res)
elif ans == '5':
    res = calculator.multiply()
    print(res)
else:
    print('неверная операция')