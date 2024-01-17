from django.core.management.base import BaseCommand
from datetime import date

from app_1.models import Client


class Command(BaseCommand):
    help = "Generate fake clients"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'name {i}', email=f'name{i}@example.com', phone=55555555 + i,
                            address=f'Moscow, Tverskaya {3 + i}', date=date.today())
            client.save()
            self.stdout.write(f'{client}')
