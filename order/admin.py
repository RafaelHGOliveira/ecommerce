from django.contrib import admin
from order import models

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass
    list_display = ('id', 'user', 'modified_at', 'created_at', )
    search_fields = ('id', 'user', )
    list_filter = 'modified_at', 'created_at',
