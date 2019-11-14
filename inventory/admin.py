from django.contrib import admin
from .models import Product, Category, ProductType, Manufacturer

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductType)
admin.site.register(Manufacturer)
