from django.contrib import admin
from product import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modified_at', 'created_at', )
    list_editable = ('name', )
    search_fields = ('name', )
    list_filter = 'active', 'modified_at', 'created_at', 
    readonly_fields = 'modified_at', 'created_at',

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
    list_display_links = 'id', 'name', 
    list_editable = 'price', 'stock',
    search_fields = ('id', 'name', )
    inlines = [PictureInline]  # Embed PictureInline in ProductAdmin
    list_filter = 'active', 'modified_at', 'created_at', 
    readonly_fields = 'modified_at', 'created_at',
