from rest_app.choices import CATEGORY_CHOICES
from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Product Name', help_text=_('Enter the name of the product'))
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Price',
                                help_text=_('Enter the price of the product'))
    stock = models.IntegerField(verbose_name='Stock', help_text=_('Enter the stock of the product'))
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, null=True, choices=CATEGORY_CHOICES, verbose_name='Category',
                                 help_text=_('Enter the category of the product'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class Category(models.Model):
    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES, verbose_name='Category name', help_text=_('Enter the name of the category'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
