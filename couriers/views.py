from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from couriers.models import Courier
from couriers.serializers import CourierSerializer, StartWorkingSerializer
from couriers.services import CourierService


class CourierViewSet(ModelViewSet):
    ACTION_MAP = {
        'default': CourierSerializer,
        'start_working': StartWorkingSerializer
    }

    queryset = Courier.objects.all()
    serializer_class = CourierSerializer
    lookup_field = 'id'

    def get_serializer_class(self):
        return self.ACTION_MAP.get(self.action, self.ACTION_MAP.get('default'))

    @action(methods=['POST'],
            detail=True,
            url_path='start_working',
            url_name='start_working',
            )
    def start_working(self, request):
        courier = self.get_object()
        serializer = self.get_serializer(request.data)
        service = CourierService(courier)
        service.start_working(current_location=request.data.get('current_location'))
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
