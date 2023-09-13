from django.urls import path, include
from .views import OrderView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('orders', OrderView)

urlpatterns = [
    path('', include(router.urls))
]