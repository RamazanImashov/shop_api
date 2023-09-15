from rest_framework import viewsets, filters, generics
from rest_framework.response import Response
from .models import Category, ProductImage, Product
from .serializers import CategorySerializer, ProductDetailSerializer, ProductListSerializer, ProductImageSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .permissions import IsAdminPermission, IsAuthorPermission
from rest_framework.decorators import action
from apps.review.serializers import LikeSerializer, DisLikeSerializer, FavoritesSerializer, RatingActionSerializer
from apps.review.models import Like, Dislike, Favorites
import django_filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


# Create your views here.

class PermissionMixin:
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy', 'create'):
            permissions = [IsAdminUser]
        else:
            permissions = [AllowAny]
        return [permissions() for permissions in permissions]


class CategoryView(PermissionMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(PermissionMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'in_stock', 'price']
    search_fields = ['slug', 'title', 'price']
    ordering_fields = ['created_at', 'title']

    @method_decorator(cache_page(60 * 5))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 5))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductDetailSerializer

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def rating(self, request, pk=None):
        product = self.get_object()
        user = request.user
        serializer = RatingActionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product, author=user)
            message = 'rating'
            return Response(message, status=200)

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        product = self.get_object()
        user = request.user
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                like = Like.objects.get(product=product, author=user)
                like.delete()
                message = 'Unlike'
            except Like.DoesNotExist:
                Like.objects.create(product=product, author=user)
                message = 'Like'
            return Response(message, status=200)

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def dislike(self, request, pk=None):
        product = self.get_object()
        user = request.user
        serializer = DisLikeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                dislike = Dislike.objects.get(product=product, author=user)
                dislike.delete()
                message = 'UnDislike'
            except Dislike.DoesNotExist:
                Dislike.objects.create(product=product, author=user)
                message = 'DisLike'
            return Response(message, status=200)

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def favorites(self, request, pk=None):
        product = self.get_object()
        user = request.user
        serializer = FavoritesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                favorites = Favorites.objects.get(product=product, author=user)
                favorites.delete()
                message = 'UnFavorites'
            except Favorites.DoesNotExist:
                Favorites.objects.create(product=product, author=user)
                message = 'Favorites'
            return Response(message, status=200)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAdminPermission]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthorPermission]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()


class ProductImageView(generics.CreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminUser]

