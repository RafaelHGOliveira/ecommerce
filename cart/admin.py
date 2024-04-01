from django.contrib import admin
from cart import models

@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    pass