import unittest


def add_numbers(number1, number2):
    return number1 + number2

class Calc:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        self.operations = 0

    def add(self):
        self.operations += 1
        return self.number1 + self.number2

    def subtract(self):
        self.operations += 1
        return self.number1 - self.number2

    def multiply(self):
        self.operations += 1
        return self.number1 * self.number2

    def divide(self):
        if self.number2 == 0:
            return 'нельзя делить на ноль'
        else:
            return self.number1 / self.number2

class MyTestCase(unittest.TestCase):
    def test_add_class(self):
        c = Calc(1, 5)
        res1 = c.add()
        self.assertEqual(res1, 6)

    def test_subtract_class(self):
        c = Calc(1, 5)
        res = c.subtract()
        self.assertEqual(res, -4)

    def test_multiply_class(self):
        c = Calc(1, 5)
        res = c.multiply()
        self.assertEqual(res, 5)

    def test_divide_class(self):
        c = Calc(4, 2)
        self.assertEqual(c.divide(), 2)

    def test_divide_zero(self):
        c = Calc(4, 0)
        self.assertEqual(c.divide(), 'нельзя делить на ноль')


    def test_operations(self):
        c = Calc(4, 5)
        c.add()
        c.add()
        c.add()
        self.assertEqual(c.operations, 3)


unittest.main()

