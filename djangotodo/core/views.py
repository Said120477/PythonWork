from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, Product

# Create your views here.
todo = [{'id': 1, 'name': 'купить подарки'},
        {'id': 2, 'name': 'поставить ёлку'}]


def main(request):
    status = request.GET.get('status')
    print(status)
    # получить все задачи
    todo = Task.objects.all()

    if status:
        # отфильтровать задачи
        todo = todo.filter(status=status)


    # добавить новую задачу
    print(request.POST)
    if request.method == 'POST':
        text_data = request.POST['text']
        descr_data = request.POST['descr']

        if text_data and descr_data:
            Task.objects.create(name=text_data, descr=descr_data)




    return render(request, 'main.html', {'todo': todo})

def about(request):
    return HttpResponse('<h2>разработка академии</h2>')

def prods(request):

    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        Product.objects.create(name=name, price=price)

        return redirect('products')
       # descr_data = request.POST['descr']


    # products = [{'id': 1, 'name': 'яблоко', 'price': 50},
    #             {'id': 2, 'name': 'апельсин', 'price': 20},
    #             {'id': 3, 'name': 'груша', 'price': 100},
    #             {'id': 4, 'name': 'виноград', 'price': 150}, ]

    prods = Product.objects.all()
    #prods = Product.objects.filter(price__gt=50, name='груша')

    return render(request, 'prods.html', {'my_products': prods})

def task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        status = request.POST['status']
        task.status = status
        task.save()
    return render(request, 'task.html', {'task': task})





