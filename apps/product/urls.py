from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('product', ProductView)
router.register('category', CategoryView)


urlpatterns = [
    path('', include(router.urls)),
    path('add-product-image/', ProductImageView.as_view())
    # path('category/', CategoryView.as_view({'get': 'list', 'post': 'create'})),
    # path('category/<slug:pk>/', CategoryView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}))
]