class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 50
        self.foot_to_it = ['мясо', 'корм', 'печеньки']
        self.friend = None
        self.human = None

    def eat(self, food):
        if food in self.foot_to_it:
            self.health += 5
            print('Спасибо')
        else:
            print('Я такое не ем')

    def wolk(self):
        self.health += 5
        print('Ура, я погулял!')

    def get_human_age(self):
        return self.age * 7

    def get_friend(self, dog):
        if abs(dog.age - self.age) < 3:
            print('Теперь ты мой друг')
            self.friend = dog
            dog.friend = self


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 60
        self.dog = None

    def add_dog(self, dog):
        if not dog.human and not self.dog:
            self.dog = dog
            dog.human = self
            print('мы подружились!')
        else:
            print('не получится')




dog1 = Dog(name='Тузик', age=2)
dog2 = Dog(name='Чарли', age=4)
human = Human(name='Джек', age=23)
human.add_dog(dog1)
human.add_dog(dog2)

dog1.get_friend(dog2)
print(dog2.friend.name)
print(dog1.friend.name)
dog1.eat('мясо')
dog1.eat('брокколи')
dog1.wolk()
print(dog1.health)
print(dog1.get_human_age())

