import graphene
from graphene_django.types import DjangoObjectType
from .models import HomepageSlider

class HomepageSliderType(DjangoObjectType):
    class Meta:
        model = HomepageSlider

    image_url = graphene.String()        
    
    def resolve_image_url(self, info):
        return "http://localhost:8000%s" % self.image.url


class Query(object):
    all_sliders = graphene.List(HomepageSliderType)

    def resolve_all_sliders(self, info, **kwargs):
        return HomepageSlider.objects.all().order_by("-pk")