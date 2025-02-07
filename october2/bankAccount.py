class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, sum):
        self._balance += sum
        print(f'добавили {sum}')

    def withdraw(self, sum):
        if sum >= self._balance:
            print('не хватает денег для снятия!')
        else:
            self._balance -= sum

    def _get_balance(self):
        print(f'баланс равен {self._balance}')
        return self._balance


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(self.accounts)

    def get_all_sum(self):
        sum = 0
        for account in self.accounts:
            sum += account._get_balance()
            print(f'всего на балансе {sum}')


account1 = BankAccount('Tom', 100)
account2 = BankAccount('jek', 200)

bank = Bank()

bank.add_account(account1)
bank.add_account(account2)
bank.get_all_sum()
