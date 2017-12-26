"""
Data models
===========
"""
from django.db import models


class Currency(models.Model):
    """
    Currency model implementation.
    """
    #: International currency 3-chars code, like "EUR"
    code = models.CharField(max_length=3, unique=True)
    # TODO: I might need to set this field to choice field
    # because i intend only support 3 currencies
    #: For example $
    symbol = models.CharField(max_length=1)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ('code', )
