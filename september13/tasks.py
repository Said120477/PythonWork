import random
class RedButton:
    def __init__(self):
        self.clicks = 0
    def click(self):
        print('тревога!!!')
        self.clicks += 1

    def count(self):
        return self.clicks

    def bang(self):
        bum = random.randint(0, 1)
        if bum == 0:
            print('BUM!!!!!')
        print('Бума не будет!')

first_button = RedButton()
second_button = RedButton()
first_button.click()
second_button.click()
first_button.bang()
second_button.bang()
for i in range(5):
    if i % 2 == 0:
        first_button.click()
    else:
        second_button.click()
print(first_button.count(), second_button.count())











