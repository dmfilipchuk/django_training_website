from django.db import models

# Create your models here.


class StatusCRM(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name= 'Название статуса')

    def __str__(self): #вернуть имя в строки
        return self.Status_name

    class Meta():
        verbose_name = 'Статус'
        verbose_name_plural= 'Статусы'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True) #дата автоматически фиксируется в момент создания экз класса
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    #след поле особое, оно привязано к классу StatusCRM, StatusCRM - родитель поля
    order_status = models.ForeignKey(StatusCRM, on_delete= models.PROTECT, null=True, blank=True, verbose_name= 'Статус')
    #PROTECT запрещает удалять элементы полей


    def __str__(self): #вернуть имя в строки
        return self.order_name

    class Meta():
        verbose_name = 'Заказ'
        verbose_name_plural= 'Заказы'

class CommentCRM(models.Model):
    coment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    coment_text = models.TextField(verbose_name='Текст комментария')
    coment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self): #вернуть имя в строки
        return self.coment_text

    class Meta():
        verbose_name = 'Комментарий'
        verbose_name_plural= 'Комментарии'