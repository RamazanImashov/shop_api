from rest_framework import viewsets
from .models import *
from .serializers import CategorySerializer, ProductSerializer


# Create your views here.


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer