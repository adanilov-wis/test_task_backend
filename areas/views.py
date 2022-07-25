from rest_framework.viewsets import ModelViewSet

from areas.models import Area
from areas.serializers import AreaSerializer


class AreaViewSet(ModelViewSet):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()
    lookup_field = 'id'
