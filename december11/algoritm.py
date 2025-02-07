data = [12, 4, 65, 3, 1, 12, 24]

# сортировка пузырьком
# for i in range(len(data)):
#     for i in range(len(data) - 1):
#         if data[i+1] < data[i]:
#             el = data.pop(i+1)
#             data.insert(i, el)
# print(data)

# быстрая сортировка (n log n)
def quick_sort(data):
    if len(data) <= 1:
        return data
    op = data[len(data)//2]
    print(op)

    left = []
    right = []
    middle = []
    for number in data:
        if number < op:
            left.append(number)
        elif number > op:
            right.append(number)
        else:
            middle.append(number)
    print(left, middle, right)
    return quick_sort(left) + middle + quick_sort(right)


quick_sort(data)
print(quick_sort(data))