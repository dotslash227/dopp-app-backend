import graphene
import inventory.schema
import promotions.schema
import orders.schema

class Query(
    inventory.schema.Query,
    promotions.schema.Query,
    orders.schema.Query,
    graphene.ObjectType):
    pass

class Mutation(
    inventory.schema.Mutation,
    orders.schema.Mutation,
    graphene.ObjectType):
    pass    

schema = graphene.Schema(query=Query, mutation=Mutation)