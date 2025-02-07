class Bank:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, money):
        if money < 0:
            raise ValueError('некорректная сумма')
        self.balance += money
        print(f'положил {money}')

    def withdraw(self, money):
        if money < 0:
            raise ValueError('сумма должна быть больше нуля')
        if money  > self.balance:
            raise ValueError('у вас нету столько денег')
        self.balance -= money
        print(f'снял {money}')

account = Bank('Артем', 100)

while True:
    print('что хочешь сделать? ')
    print('1 - пополнить')
    print('2 - снять')
    print('q - выход')

    ans = input('выбери действие: ')
    try:
        if ans == '1':
            money = int(input('введи сумму: '))
            account.deposit(money)
        elif ans == '2':
            money = int(input('введи сумму для снятия: '))
            account.withdraw(money)
        elif ans == 'q':
            break

    except ValueError as e:
        print(f'ошибка {e}')


