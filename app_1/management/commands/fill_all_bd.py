from django.core.management.base import BaseCommand

from app_1.models import Client, Product, Order
from random import randint
class Command(BaseCommand):
    help = 'fill db'

    def add_arguments(self, parser):
        parser = parser.add_argument('count', type=int, help='count')


    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        clients = Client.objects.all()
        for client in clients:
            for i in range(1, count + 1):
                order = Order(client=client)
                total = 0
                for j in range(1, count + 1):
                    product = Product(name=f'product{randint(1, 1000000)}', price=randint(10, 1000))
                    total += product.price
                    product.save()
                    order.save()
                    order.products.add(product)
                order.total_price = total
                order.save()





