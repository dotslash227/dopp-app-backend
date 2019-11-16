import graphene
from graphene_django.types import DjangoObjectType
from .models import HomepageSlider

class HomepageSliderType(DjangoObjectType):
    class Meta:
        model = HomepageSlider


class Query(object):
    all_sliders = graphene.List(HomepageSliderType)

    def resolve_all_sliders(self, info, **kwargs):
        return HomepageSlider.objects.all().order_by("-pk")