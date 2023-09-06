from rest_framework import viewsets
from .models import *
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.permissions import IsAdminUser, AllowAny


# Create your views here.

# class PermissionMixin:
#     def get_permissions(self):
#         if self.action in ('update', 'partial_update', 'destroy', 'create'):
#             permissions = [IsAdminUser]
#         else:
#             permissions = [AllowAny]
#         return [permissions() for permissions in permissions]


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
