class AmountError(ValueError):
    pass
def deposit(money, balance):
    if money < 0:
        raise AmountError('Сумма должна быть положительной')
    balance += money
    return balance

balance = 0

while True:
    try:
        money = int(input('сколько денег закинуть? '))
        balance = deposit(money, balance)
    except ValueError:
        print('некорректный ввод')
    except AmountError as e:
        print(f'что то пошло не так...{e}')
    print(f'твой баланс {balance}')
