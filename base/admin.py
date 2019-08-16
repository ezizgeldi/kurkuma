from django.contrib import admin
from base.models import Category, Brand, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name', )}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug':('title', )}




admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
