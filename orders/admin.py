from django.contrib import admin
from .models import Order, Transaction, OrderLine

class OrderLineTabularInline(admin.TabularInline):
    model = OrderLine
    extra = 2
    readonly_fields = ["total"]

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineTabularInline]
    readonly_fields = ["sub_total", "total"]

admin.site.register(Order, OrderAdmin)
admin.site.register(Transaction)
admin.site.register(OrderLine)
