from rest_framework.viewsets import ModelViewSet

from orders.models import Order
from orders.serializers import OrderSerializer, OrderCreateSerializer


class OrderViewSet(ModelViewSet):
    ACTION_MAP = {
        'default': OrderSerializer,
        'create': OrderCreateSerializer
    }

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        return self.ACTION_MAP.get(self.action, self.ACTION_MAP.get('default'))

