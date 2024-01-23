from django import forms
from datetime import date
from .models import Product

# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=150)
#     description = forms.CharField(max_length=250)
#     price = forms.DecimalField(max_digits=8, decimal_places=2)
#     amount = forms.IntegerField(default=1)
#     date = forms.DateField(default=date(year=2001, month=1, day=21))


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'amount', 'date', 'photo']

    product_ = forms.ModelChoiceField(queryset=Product.objects.all())


class NewProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'amount', 'date', 'photo']


