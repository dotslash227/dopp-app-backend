from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from inventory.models import Product


class Order(models.Model):
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    products = models.ManyToManyField(Product)
    sub_total = models.FloatField(default=0.00)
    tax = models.FloatField(default=0.00)
    shipping = models.FloatField(default=0.00)
    discount = models.FloatField(default=0.00)
    total = models.FloatField(default=0.00)
    status = models.CharField(max_length=50, default="In Process", choices=(
        ("In Process", "In Process"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered")        
    ))
    courier = models.CharField(max_length=100)
    tracking_number = models.CharField(max_length=100)
    remarks = models.TextField(blank=True, null=True)


class Transaction(models.Model):
    date = models.DateTimeField(default=timezone.now)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount = models.FloatField(default=0.00)
    mode = models.CharField(max_length=30, choices=(
        ("Online", "Online"),
        ("Offline", "Offline")
    ))
    reference_number = models.CharField(max_length=100)
    method = models.CharField(max_length=100)