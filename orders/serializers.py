from rest_framework import serializers


from orders.models import Order
from orders.service import OrderService


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    area = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    def save(self, **kwargs):
        service = OrderService(instance=self.instance)
        self.area = service.get_area(destination=self.validated_data.get('destination'))
        service.set_courier(area=self.area)
        return super().save(**kwargs)

    class Meta:
        model = Order
        exclude = ['courier']
