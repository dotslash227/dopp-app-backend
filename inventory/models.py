from django.db import models
from django.utils import timezone

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    date_added = models.DateField(default=timezone.now)
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING, blank=True, null=True)
    categories = models.ManyToManyField(Category)
    mrp = models.FloatField(default=0.00)
    discount = models.FloatField(default=0.00)
    sale_price = models.FloatField(default=0.00)
    available = models.BooleanField(default=False, choices=(
        (True, "Yes"),
        (False, "No")
    ))

    def __str__(self):
        return self.name

