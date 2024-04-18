from django.db import models
from product.models import Product


# Create your models here.
class Cart(models.Model):
    products = models.ManyToManyField(Product)

    class Meta:
        verbose_name = 'Carrinho'
        verbose_name_plural = 'Carrinhos'
