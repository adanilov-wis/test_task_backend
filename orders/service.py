from typing import Optional, Iterable

from django.contrib.gis.geos import Point
from django.db.models import Count

from areas.models import Area
from couriers.models import Courier
from orders.models import Order


class OrderService:
    """
    Service for managing operations with Order instance
    """
    def __init__(self, instance: Optional[Order]):
        self.instance = instance

    @staticmethod
    def get_area(destination: Iterable[float]) -> Area:
        """
        Get area that contains given destionation point
        """
        return Area.objects.filter(geom__contains=Point(destination)).first()

    def set_courier(self, area: Area):
        """
        Set less busy courier for order
        """
        relevant_couriers = Courier.objects.filter(area=area, is_working=True)
        less_busy_courier = relevant_couriers.annotate(num_orders=Count('orders')).order_by('num_orders').first()
        self.instance.courier = less_busy_courier
        self.instance.save()
