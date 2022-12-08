from django.contrib import admin
from .models import Order, StatusCRM, CommentCRM

# Register your models here.
class Coment(admin.StackedInline):
    model = CommentCRM
    fields = ('coment_dt', 'coment_text')
    readonly_fields = ('coment_dt', )
    extra = 1 #будет отображаться только один комментарий


class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    list_filter = ('order_status',)
    list_editable = ('order_status', 'order_phone')
    list_per_page = 10
    list_max_show_all = 20
    fields = ('id', 'order_status', 'order_dt', 'order_name', 'order_phone')
    readonly_fields = ('id', 'order_dt')
    #передаем класс Coment в поле
    inlines = [Coment, ]


admin.site.register(Order, OrderAdm)
admin.site.register(StatusCRM)
admin.site.register(CommentCRM)