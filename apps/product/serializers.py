from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Category, Product, ProductImage
from apps.review.serializers import CommentSerializer
from django.db.models import Avg


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, price):
        if price <= 0:
            raise ValidationError(
                'Price not be 0 or little'
            )
        return price

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['images'] = ProductImageSerializer(instance.images.all(), many=True).data
        rep['rating'] = instance.ratings.aggregate(Avg('rating'))['rating__avg']
        rep['likes'] = instance.likes.all().count()
        rep['dislikes'] = instance.dislikes.all().count()
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        return rep


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'price', 'category']

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['rating'] = instance.ratings.aggregate.count('rating')
    #     rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
    #     return rep


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

