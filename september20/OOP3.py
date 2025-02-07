# class MyInt(int):
#     def __add__(self, other):
#         return self - other
#
# a = MyInt(4)
# b = MyInt(5)
# print(a + b)

# написать класс counter. он должен иметь методы: decrement()- уменьшить клики
# increment() - увеличить клики. если кликов больше 10, надо вызывать метод update_count,
# который сбрасывает клики на нуль

class Counter():

    def __init__(self):
        self.count = 0

    def decrement(self):
        self.count -= 1

    def increment(self):
        self.count += 1
        self._update_count()
        print(self.count)


    def _update_count(self):
        if self.count > 10:
            self.count = 0
        print(self.count)

counter = Counter()
for i in range(20):
    counter.increment()
print(counter.count)

counter.increment()











