from django.contrib.gis.db import models

from couriers.models import Courier


class Order(models.Model):
    PAID = 'Paid'
    IN_DELIVERY = 'In delivery'
    DONE = 'Done'

    STATUS_CHOICES = [
        (PAID, 'Paid'),
        (IN_DELIVERY, 'In delivery'),
        (DONE, 'Done'),
    ]

    courier = models.ForeignKey(
        Courier,
        null=False,
        related_name='orders',
        on_delete=models.CASCADE,
        verbose_name='Responsible courier'
    )
    destination = models.PointField(null=False, verbose_name='Destination point')
    status = models.CharField(
        max_length=64,
        choices=STATUS_CHOICES,
        default='Paid',
        verbose_name='Status'
    )
