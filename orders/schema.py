import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from .models import Order, OrderLine
from inventory.schema import ProductType
from inventory.models import Product

class UserType(DjangoObjectType):
    class Meta:
        model = User

class OrderLineType(DjangoObjectType):
    order_id = graphene.Int()
    product_id = graphene.Int()

    class Meta:
        model = OrderLine

    def resolve_order_id(self, info):
        return self.order.id
    def resolve_product_id(self, info):
        return self.product.id

class OrderType(DjangoObjectType):    
    user = graphene.Field(UserType)
    class Meta:
        model = Order
        
    def resolve_user(self, info):
        return self.user

class ProductInput(graphene.InputObjectType):
    id = graphene.Int()    
    quantity = graphene.Int()    
    data = graphene.String()

class CreateOrderMutation(graphene.Mutation):
    class Arguments:
        userId = graphene.Int(required=True)
        products = graphene.List(ProductInput, required=True)
    
    order = graphene.Field(OrderType)

    def mutate(self, info, userId, products):
        user = User.objects.get(pk=userId)
        order = Order.objects.create(user=user)
        for each in products:
            product = Product.objects.get(pk=each.id)
            order_line = OrderLine(order=order, product=product, price=product.sale_price, quantity=each.quantity)
            order_line.save()

        return CreateOrderMutation(order=order)


class Query(object):
    all_orders = graphene.List(OrderType)

    def resolve_all_orders(self, info, **kwargs):
        return Order.objects.all()


class Mutation(graphene.ObjectType):
    create_order = CreateOrderMutation.Field()