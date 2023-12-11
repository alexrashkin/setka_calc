from django.db import models


class SetkaOrder(models.Model):
    diameter = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    rolls = models.PositiveIntegerField()