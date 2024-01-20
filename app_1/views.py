# Создайте пару представлений в вашем первом приложении: главная и о себе.
# Внутри каждого представления должна быть переменная html - многострочный текст
# с HTML вёрсткой и данными о вашем первом Django сайте и о вас.
# *Сохраняйте в логи данные о посещении страниц

from django.http import HttpResponse
from .models import Client, Order
from django.shortcuts import render
import logging
from datetime import date, timedelta

logger = logging.getLogger(__name__)


def index(request):
    res = ('<h1>Это главная страница</h1>'
           '<h2>Здесь будет размещена информация о нашей деятельности</h2>'
           '<p>Мы предлагаем лучшие товары по самым низким ценам</p>')
    logger.info('index get request')
    return HttpResponse(res)


def contact(request):
    res = ('<h1>Наши контакты</h1>'
           '<h2>email: mail@mail.com</h2>'
           '<p>Телефон: + 7 555 55 55</p>')
    logger.info('contact get request')
    return HttpResponse(res)


def client_view(request):
    clients = Client.objects.all()
    res = '<br>'.join([str(client) for client in clients])
    return HttpResponse(res)


def all_client_orders(request, client_id=1):
    client = Client.objects.get(id=client_id)
    orders = Order.objects.filter(client=client)
    context = {'orders': orders, 'client': client}
    return render(request, 'app_1/all_client_orders.html', context=context)


def order_sort_time(request, client_id, days):
    client = Client.objects.get(id=client_id)
    orders = Order.objects.filter(client=client)
    list_orders = []
    for order in orders:
        data = order.date_created
        if data >= date.today() - timedelta(days=days):
            list_orders.append(order)
    list_orders.sort(key=lambda x: x.date_created)
    context = {
        'client': client,
        'products_': list_orders,
        'days': days,
    }
    return render(request, 'app_1/order_sort_time.html', context=context)

