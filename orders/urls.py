from django.urls import include, path
from rest_framework.routers import SimpleRouter

from orders.views import OrderViewSet

app_name = 'orders'

router = SimpleRouter()
router.register('', OrderViewSet, basename='orders')

urlpatterns = [
    path('', include(router.urls)),
]
