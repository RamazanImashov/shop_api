from rest_framework.serializers import ModelSerializer
from .models import Order, OrderItem


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


class OrderSerializer(ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'total_sum', 'items']

    def create(self, validated_data):
        items = validated_data.pop('items')
        validated_data['user'] = self.context.get('request').user
        order = super().create(validated_data)
        total_sum = 0
        orders_items = []
        for item in items:
            orders_items.append(OrderItem(
                order=order,
                product=item['product'],
                quantity=item['quantity']
            ))
            total_sum += item['product'].price * item['quantity']
        OrderItem.objects.bulk_create(orders_items)
        order.total_sum = total_sum
        order.save()
        return order
