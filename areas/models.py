from django.contrib.gis.db import models


class Area(models.Model):
    geometry = models.PolygonField(blank=False, null=False, verbose_name='Area polygon')
    name = models.CharField(max_length=64, blank=False, null=False, unique=True, verbose_name='Area name')
