def factorial_r(number):
    for i in range(1, number + 1):
        if number == 1:
            return number
        else:
            res = number * factorial_r(number - 1)
            return res

f = factorial_r(5)
print(f)


