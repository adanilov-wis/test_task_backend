from typing import Optional

from django.contrib.gis.geos import Point

from areas.models import Area
from couriers.models import Courier


class CourierService:
    """
    Service for managing operations with Courier instance
    """

    def __init__(self, instance: Optional[Courier]):
        self.instance = instance

    def start_working(self, current_location):
        self.instance.is_working = True
        self.instance.area = self._get_related_area(current_location)
        self.instance.save()

    @staticmethod
    def _get_related_area(current_location) -> Area:
        """
        Get area for courier`s current location
        """
        location_point = Point(current_location)
        area = Area.objects.filter(geom__contains=location_point).first()
        return area
