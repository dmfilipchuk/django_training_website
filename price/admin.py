from django.contrib import admin
from .models import PriceCard
from .models import PriceTable

# Register your models here.
admin.site.register(PriceCard) #регистрируем оба класса в админке
admin.site.register(PriceTable)