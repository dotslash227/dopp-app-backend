import graphene
import inventory.schema

class Query(
    inventory.schema.Query,
    graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)