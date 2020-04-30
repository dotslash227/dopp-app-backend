import graphene
import inventory.schema
import promotions.schema
import orders.schema
import authentication.schema

class Query(
    inventory.schema.Query,
    promotions.schema.Query,
    orders.schema.Query,
    authentication.schema.Query,
    graphene.ObjectType):
    pass

class Mutation(
    inventory.schema.Mutation,
    orders.schema.Mutation,
    authentication.schema.Mutation,
    graphene.ObjectType):
    pass    

schema = graphene.Schema(query=Query, mutation=Mutation)