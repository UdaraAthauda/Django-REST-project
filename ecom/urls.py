from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', views.ProductView, basename="products")

urlpatterns = [
    path('', include(router.urls))
]
