import graphene
from graphene_django.types import DjangoObjectType
from .models import Product, Category, Manufacturer
from .models import ProductType as product_type

class ManufacturerType(DjangoObjectType):
    class Meta:
        model = Manufacturer

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class PTType(DjangoObjectType):
    class Meta:
        model = product_type

class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class ProductMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        mrp = graphene.Float()
        discount = graphene.Float()
        available = graphene.Boolean()

    product = graphene.Field(ProductType)
    def mutate(self, info, id, mrp=0.00, discount=0.00, available=False):
        product =  Product.objects.get(pk=id)
        if mrp != 0:
            product.mrp = mrp            
        if discount != 0:
            product.discount = discount
        if available or product.available:
            product.available = True
        product.save()

        return ProductMutation(product=product)

class Mutation(graphene.ObjectType):
    update_product = ProductMutation.Field()


class Query(object):    
    all_categories = graphene.List(CategoryType)
    manufacturer = graphene.Field(ManufacturerType, id=graphene.Int(), name=graphene.String())
    all_manufacturers = graphene.List(ManufacturerType)
    product = graphene.Field(ProductType, id=graphene.Int(), name=graphene.String())
    products = graphene.List(ProductType, category=graphene.Int(), manufacturer=graphene.Int(), available=graphene.Boolean())
    all_products = graphene.List(ProductType)
    all_product_types = graphene.List(PTType)    

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()
    def resolve_all_manufacturers(self, info, **kwargs):
        return Manufacturer.objects.all()
    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()
    def resolve_all_product_types(self, info, **kwargs):
        return product_type.objects.all()
    def resolve_product(self, info, **kwargs):
        id = kwargs.get("id")
        name = kwargs.get("name")
        if id is not None:
            return Product.objects.get(id=id)
        if name is not None:
            return Product.objects.get(name=name)
    def resolve_products(self, info, **kwargs):
        category = kwargs.get("category")
        manufacturer = kwargs.get("manufacturer")
        available = kwargs.get("available")
        products = Product.objects.all()

        if category is not None:            
            category_ob = Category.objects.get(pk=category)            
            products = products.filter(categories=category_ob)
        if manufacturer is not None:            
            manufacturer_ob = Manufacturer.objects.get(id=manufacturer)
            products = products.filter(manufacturer=manufacturer_ob)
        if available is not None:
            products = products.filter(available=available)

        return products

    def resolve_manufacturer(self, info, **kwargs):
        id = kwargs.get("id")
        name = kwargs.get("name")
        if id is not None:
            return Manufacturer.objects.get(id=id)
        if name is not None:
            return Manufacturer.objects.get(name=name)