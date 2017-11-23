"""Model classes for money app."""
from django.db import models


class Currency(models.Model):
    """Currency implementation."""
    code = models.CharField(max_length=3, unique=True)
    symbol = models.CharField(max_length=1)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ('code', )
