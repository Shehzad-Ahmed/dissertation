from django.urls import path, include
from rest_framework import routers

from inventory import views

router = routers.DefaultRouter()

router.register("products/search", viewset=views.ProductsSearchViewSet, basename="products-search")

urlpatterns = [
    path("", include(router.urls))
]
