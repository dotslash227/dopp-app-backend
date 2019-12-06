from django.contrib import admin
from .models import Product, Category, ProductType, Manufacturer, Power, Axis

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ["sale_price"]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductType)
admin.site.register(Manufacturer)
admin.site.register(Power)
admin.site.register(Axis)