from django.db import models

# Create your models here.

class PriceCard(models.Model):
    pc_value = models.CharField(max_length= 20, verbose_name= 'Цена')
    pc_descrption = models.CharField(max_length=200, verbose_name='Описание')


    def __str__(self): #вернуть имя в строки
        return self.pc_value

    class Meta():
        verbose_name = 'Цены'
        verbose_name_plural= 'Цены'


class PriceTable(models.Model):
    pt_title = models.CharField(max_length= 200, verbose_name= 'Услуга')
    pt_new_price = models.CharField(max_length=200, verbose_name='Новая цена')
    pt_old_price = models.CharField(max_length=200, verbose_name='Старая цена')


    def __str__(self): #вернуть имя в строки
        return self. pt_title

    class Meta():
        verbose_name = 'Услугу'
        verbose_name_plural= 'Услуги'
