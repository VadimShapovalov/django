from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    address = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Client's name: {self.name}, email: {self.email}"


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


