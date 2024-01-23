# Создайте пару представлений в вашем первом приложении: главная и о себе.
# Внутри каждого представления должна быть переменная html - многострочный текст
# с HTML вёрсткой и данными о вашем первом Django сайте и о вас.
# *Сохраняйте в логи данные о посещении страниц

from django.http import HttpResponse
from .models import Client, Order, Product
from django.shortcuts import render
import logging
from datetime import date, timedelta
from .forms import ProductForm, NewProductForm
from django.core.files.storage import FileSystemStorage

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


def products_from_order(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'app_1/products_from_order.html', context={'order': order})


def update_product(request):
    # product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            product = form.cleaned_data['product_']

            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            amount = form.cleaned_data['amount']
            date = form.cleaned_data['date']
            photo = form.cleaned_data['photo']
            logger.info(f'Update {product.name}')
            message = 'product update'
            product.name = name
            product.description = description
            product.price = price
            product.amount = amount
            product.date = date
            product.photo = photo
            fs = FileSystemStorage()
            fs.save(product.name, photo)
            product.save()
    else:
        form = ProductForm()
        message = 'Заполните форму'
    context = {
        'form': form,
        'message': message,
    }
    return render(request, 'app_1/update_product.html', context=context)


def create_product(request):
    # product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            # product = form.cleaned_data['product_']

            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            amount = form.cleaned_data['amount']
            date = form.cleaned_data['date']
            photo = form.cleaned_data['photo']
            logger.info(f'Create {name=}')
            message = 'product created successfully'
            product = Product(name=name, description=description, price=price, amount=amount, date=date, photo=photo)
            fs = FileSystemStorage()
            fs.save(product.name, photo)
            product.save()
    else:
        form = NewProductForm()
        message = 'Заполните форму'
    context = {
        'form': form,
        'message': message,
    }
    return render(request, 'app_1/create_product.html', context=context)
