from django.db import models

# Create your models here.
class Task(models.Model):
    UNCOMPLETE = 'uncomplete'
    COMPLETE = 'complete'
    INPROCESS = 'inprocess'
    STATUS_CHOICES = [
        (UNCOMPLETE, "не выполнена"),
        (COMPLETE, "выполнена"),
        (INPROCESS, "в процессе")
    ]
    name = models.CharField(max_length=100, verbose_name='Название')
    descr = models.TextField(verbose_name='описание', blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=UNCOMPLETE)
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.IntegerField(verbose_name='цена')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} - {self.price}'