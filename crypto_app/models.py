# Create your models here.
from curses.ascii import CR
from doctest import DONT_ACCEPT_BLANKLINE
from pyexpat import model
from django.conf import settings
from django.db import models
from django.template.defaulttags import now
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CryptoCurrency(models.Model):
    name = models.CharField(max_length=30, null=True)
    carbon_foot_print = models.FloatField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    update = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    class Meta:
        unique_together = (('user', 'cryptoCurrency'),)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cryptoCurrency = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE, null=True)
    solde = models.FloatField(null=True)

    def __str__(self):
        return "Account " + str(self.user)

class Transactions(models.Model):
    class Meta:
        unique_together = (('user','cryptoCurrency','value','date'),)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    #users = models.ManyToManyField(User)
    cryptoCurrency = models.ForeignKey(CryptoCurrency, on_delete=models.DO_NOTHING, null=True)
    value = models.FloatField(null=True)
    date = models.DateTimeField(null=True)
    footPrint = models.FloatField(null=True)
    
    def __str__(self):
        return "Transaction " + str(self.user) + " " + str(self.value)

