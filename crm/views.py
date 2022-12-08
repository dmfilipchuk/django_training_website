from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sendthemessage import sendTelegram


# Create your views here.
def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1) #получаем переменную при помощи метода GET по ID
    pc_2 = PriceCard.objects.get(pk=2) #получаем переменную при помощи метода GET по ID
    pc_3 = PriceCard.objects.get(pk=3) #получаем переменную при помощи метода GET по ID
    price_table = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {'slider_list': slider_list,
                'pc_1': pc_1,
                'pc_2': pc_2,
                'pc_3': pc_3,
                'price_table': price_table,
                'form': form}
    return render(request, './index.html', dict_obj)



def thanks(request):
    if request.POST:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        element = Order(order_name = name, order_phone = phone) #создаем экземпляр класса
        element.save()
        sendTelegram(tg_name = name, tg_phone = phone)
        return render(request, './thanks.html', {'name': name,
                                               'phone': phone})
    else:
        return render(request, './thanks.html')