# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class CryptoCurrency(models.Model):
    name = models.CharField(max_length=30, null=True)
    carbon_foot_print = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    name = models.FloatField(max_length=30, null=True)

