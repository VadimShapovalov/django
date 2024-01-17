from django.core.management import BaseCommand
from datetime import date
from app_1.models import Client

class Command(BaseCommand):
    help = 'Create a new client'

    def handle(self, *args, **kwargs):
        client = Client(name='Bob', email='bob@example.com', phone=55555555,
                        address='Moscow, Tverskaya 3 98', date=date.today())
        client.save()
        self.stdout.write(f'{client}')

