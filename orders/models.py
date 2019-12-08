from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from inventory.models import Product


class Order(models.Model):
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)    
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
    courier = models.CharField(max_length=100, blank=True, null=True)
    tracking_number = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Order no. %s of user %s" % (self.pk, self.user.id)

    def save(self, *args, **kwargs):            
        discounted = self.sub_total - self.sub_total*self.discount/100
        self.total = discounted + discounted*self.tax/100 + self.shipping
        super(Order, self).save(*args, **kwargs)

class OrderLine(models.Model):
    date = models.DateTimeField(default=timezone.now)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)
    total = models.FloatField(default=0.00)
    data = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total = self.quantity * self.price
        self.order.sub_total = self.order.sub_total + self.total
        self.order.save()
        super(OrderLine, self).save(*args, **kwargs)


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