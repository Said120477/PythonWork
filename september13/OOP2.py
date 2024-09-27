# Задание 1
# Продолжите работать над программой из прошлой домашки. Добавьте
# новый класс SportCar(), который наследуется от базового класса Car( )
# Внутри класса SportCar() создайте метод fast_drive(), который будет
# работать также как drive(), только потребление топлива сделайте в
# полтора раза больше.
# Дополните класс методом competition() суть которого в том, чтобы с
# вероятностью 50% возвращать выиграла машина в соревнованиях или
# нет
import random
class Car:
    def __init__(self, color, fuel, consumption, mileage=0, ):
        self.color = color
        self.fuel = fuel
        self.consumption = consumption
        self.mileage = mileage
        print(f'создали машину {self.color, self.fuel}')
        self.is_clean = False

    def drive(self, km):
        need_fuel = (km * self.consumption)/100
        if need_fuel <= self.fuel:
            print(f'мы проехали {km} км')
            self.fuel -= need_fuel
            self.mileage += km
        else:
            print('не доедем :)')

    def get_mileage(self):
        return self.mileage

    def clean(self):
        self.is_clean = True


class SportCar(Car):
    def fast_drive(self, km):
        need_fuel = (km * self.consumption * 1.5) / 100
        if need_fuel <= self.fuel:
            print(f'мы проехали {km} км')
            self.fuel -= need_fuel
            self.mileage += km
        else:
            print('не доедем :)')

    def clean(self):
        if self.is_clean == False:
            print('она уже чистая')
        else:
            self.is_clean = True

    def competition(self):
        if random.choice([True, False]):
            print("Машина выиграла соревнование!")
            return True
        else:
            print("Машина не выиграла соревнование.")
            return False


car = Car(color='yellow', fuel=20, consumption=5)
sport_car = SportCar(color='red', fuel=20, consumption=15)

for i in range(6):
    car.drive(100)
    car.drive(80)
print(car.get_mileage())
sport_car.fast_drive(50)
sport_car.clean()

sport_car.competition()