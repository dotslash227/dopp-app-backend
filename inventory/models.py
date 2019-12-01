from django.db import models
from django.utils import timezone

class Power(models.Model):
    power = models.FloatField()

    def __str__(self):
        return "%s" % str(self.power)

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
    description = models.TextField(blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING, blank=True, null=True)
    categories = models.ManyToManyField(Category)
    mrp = models.FloatField(default=0.00)
    discount = models.FloatField(default=0.00)
    sale_price = models.FloatField(default=0.00)
    image = models.FileField(max_length=100, upload_to="products", blank=True, null=True)
    build = models.CharField(max_length=10, choices=(
        ("spherical", "Spherical"),
        ("toric", "Toric")
    ), default="spherical")
    sph_powers = models.ManyToManyField(Power, related_name="sph_powers")
    cyl_powers = models.ManyToManyField(Power, related_name="cyl_powers")
    available = models.BooleanField(default=False, choices=(
        (True, "Yes"),
        (False, "No")
    ))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.sale_price = self.mrp - self.mrp*self.discount/100
        super(Product, self).save(*args, **kwargs)

