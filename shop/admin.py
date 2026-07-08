from .models import (
    Product,
    Category,
    Contact,
) 

from django.contrib import admin


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'category',
                    'price',
                    'is_featured',
                    'created_at'
                    )
    search_fields = ('name', 'description','category__name')
    list_filter = ('category', 'is_featured', 'created_at')
    ordering = ('created_at',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject',)
    search_fields = ('name', 'email', 'subject')