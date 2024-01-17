# Создайте пару представлений в вашем первом приложении: главная и о себе.
# Внутри каждого представления должна быть переменная html - многострочный текст
# с HTML вёрсткой и данными о вашем первом Django сайте и о вас.
# *Сохраняйте в логи данные о посещении страниц

from django.http import HttpResponse
from .models import Client
from django.shortcuts import render
import logging

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
