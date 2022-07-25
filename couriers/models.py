from django.contrib.gis.db import models

from areas.models import Area


class Courier(models.Model):
    area = models.ForeignKey(Area, null=True, blank=True, on_delete=models.CASCADE, related_name='couriers')
    is_working = models.BooleanField(default=False, null=False)
