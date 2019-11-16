from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [    
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
