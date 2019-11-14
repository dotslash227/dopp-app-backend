from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Manufacturer, Category, ProductType
from .serializers import ProductSerializer, ManufacturerSerializer, CategorySerializer, ProductTypeSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset  = ProductType.objects.all()
    serializer_class = ProductTypeSerializer