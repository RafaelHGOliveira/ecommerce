from django.contrib import admin
from product import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modified_at', 'created_at', )
    list_editable = ('name', )

class PictureInline(admin.TabularInline):
    model = models.Picture
    extra = 1

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'name', 
        'price', 
        'stock', 
        'short_description',
        'category_ref', 
        'modified_at', 
        'created_at',
    )
    list_display_links = list_display
    inlines = [PictureInline]  # Embed PictureInline in ProductAdmin
