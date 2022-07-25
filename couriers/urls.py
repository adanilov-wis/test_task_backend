from django.urls import include, path
from rest_framework.routers import SimpleRouter

from couriers.views import CourierViewSet

app_name = 'couriers'

router = SimpleRouter()
router.register('', CourierViewSet, basename='couriers')

urlpatterns = [
    path('', include(router.urls)),
]
