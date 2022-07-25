from django.urls import include, path
from rest_framework.routers import SimpleRouter

from areas.views import AreaViewSet


app_name = 'areas'

router = SimpleRouter()
router.register('', AreaViewSet, basename='areas')

urlpatterns = [
    path('', include(router.urls)),
]
