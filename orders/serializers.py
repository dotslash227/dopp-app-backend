from rest_framework import serializers
from .models import Order, Transaction

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ["date", "user", "products", "sub_total", "shipping", "discount", "total", "status", "courier", "tracking_number", "remarks"]

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ["date", "user", "order", "amount", "method"]