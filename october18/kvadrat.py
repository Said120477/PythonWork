import turtle

# # Создание экземпляра класса Turtle
# t = turtle.Turtle()
#
# # Установка цвета линии
# t.pencolor("red")
#
# # Рисование квадрата
# for _ in range(4):
#     # Перемещение в начальную точку квадрата
#     t.forward(100)
#     # Поворот на 90 градусов
#     t.left(90)
#
# # Завершение программы
# turtle.done()

screen = turtle.Screen()
screen.title("Рисование квадрата") # Создание черепашки
t = turtle.Turtle()  # Функция для рисования квадрата

def draw_square(size):
    for _ in range(4):
        t.forward(size)  # Перемещение вперед на заданную длину
        t.right(90)  # Поворот вправо на 90 градусов


# Вызов функции для рисования квадрата размером 100
draw_square(200)
# Завершение работы
turtle.done()