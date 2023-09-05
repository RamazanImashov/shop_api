from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('category', CategoryView)
router.register('product', ProductView)



urlpatterns = [
    path('', include(router.urls)),
    # path('category/', CategoryView.as_view({'get': 'list', 'post': 'create'})),
    # path('category/<slug:pk>/', CategoryView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}))
]