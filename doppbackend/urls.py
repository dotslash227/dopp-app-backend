from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from authentication import views
from inventory import views as inventory

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'products',  inventory.ProductViewSet)
router.register(r'manufacturer', inventory.ManufacturerViewSet)
router.register(r'category', inventory.CategoryViewSet)
router.register(r'product-type', inventory.ProductTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),    
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
