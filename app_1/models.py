from django.db import models
from datetime import date





class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    address = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
        # return f"Client's name: {self.name}, email: {self.email}"


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField(default=1)
    date = models.DateField(default=date(year=2001, month=1, day=21))
    photo = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.name}   price: ${self.price}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    date_created = models.DateField(default=date.today())

    def __str__(self):
        return f'order №{self.pk}, client "{self.client}".'


