# Create your models here.
from django.db import models
from django.template.defaulttags import now


class CryptoCurrency(models.Model):
    name = models.CharField(max_length=30, null=True)
    carbon_foot_print = models.FloatField(null=True)



