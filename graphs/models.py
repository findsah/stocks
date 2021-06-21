from django.db import models


# Create your models here.
class Stocks(models.Model):
    SYMBOL = models.CharField(max_length=500)
    SERIES = models.CharField(max_length=1000, null=True)
    OPEN = models.CharField(max_length=1000, null=True)
    HIGH = models.CharField(max_length=1000, null=True)
    LOW = models.CharField(max_length=1000, null=True)
    CLOSE = models.CharField(max_length=1000, null=True)
    TIMESTAMP = models.CharField(max_length=1000, null=True)


    def __str__(self):
        return self.SERIES
