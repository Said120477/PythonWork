
def add_message(function, *args, **kwargs):

    def func(*args, **kwargs):
        print('кто то вызвал функцию!')
        return function(*args, **kwargs)
    return func

@add_message
def add(num1, num2):
    print(num1 + num2)

@add_message
def subtract(num1, num2):
    print(num1 - num2)


add(1, 5)
subtract(3, 2)
