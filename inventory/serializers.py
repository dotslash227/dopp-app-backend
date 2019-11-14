from rest_framework import serializers
from .models import Product, ProductType, Manufacturer, Category

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "manufacturer", "categories", "mrp", "discount", "sale_price"]

class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ["name"]

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "product_type"]

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductType
        fields = ["name"]