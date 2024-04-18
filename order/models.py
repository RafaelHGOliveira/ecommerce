from django.db import models
from customer.models import User
from product.models import Product, Base


class Order(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
