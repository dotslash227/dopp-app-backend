import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from .models import Address


# Query Classes and Object Types

class AddressType(DjangoObjectType):
    class Meta:
        model = Address


class Query(object):
    address = graphene.Field(AddressType, id=graphene.Int())
    user_addresses = graphene.List(AddressType, userId=graphene.Int())

    def resolve_address(self, info, **kwargs):
        id = kwargs.get("id")        
        return Address.objects.get(pk=id)

    def resolve_user_addresses(self, info, **kwargs):        
        user_id = kwargs.get("userId")
        user = User.objects.get(pk=user_id)
        return Address.objects.filter(user=user)


# Mutations

class AddAddressMutation(graphene.Mutation):
    address = graphene.Field(AddressType)

    class Arguments:
        user_id = graphene.Int(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        add1 = graphene.String(required=True)
        add2 = graphene.String(required=True)
        locality = graphene.String(required=True)
        landmark = graphene.String(required=True)
        city = graphene.String(required=True)
        pincode = graphene.Int(required=True)

    def mutate(self, info, user_id, first_name, last_name, add1, add2, locality, landmark, city, pincode):
        user = User.objects.get(pk=user_id)
        address = Address.objects.create(user=user, first_name=first_name, last_name=last_name, add1=add1, add2=add2, locality=locality, landmark=landmark, city=city, pincode=pincode)

        return AddAddressMutation(address=address)


class Mutation(graphene.ObjectType):
    add_address = AddAddressMutation.Field()


