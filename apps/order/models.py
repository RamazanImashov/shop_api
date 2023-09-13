from django.db import models
from django.contrib.auth import get_user_model
from apps.product.models import Product

# Create your models here.

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product, through='OrderItem')
    total_sum = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    statuses = [
        ('D', 'Delivered'),
        ('N', 'Not Delivered')
    ]
    status = models.CharField(max_length=1, choices=statuses)
    payments = [
        ('Card', 'Card'),
        ('Cash', 'Cash')
    ]
    payment = models.CharField(max_length=4, choices=payments)

    def __str__(self):
        return f'{self.pk}:{self.products}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, related_name='order_items')
    quantity = models.PositiveSmallIntegerField(default=1)

    class Meta:
        db_table = 'order_items'
