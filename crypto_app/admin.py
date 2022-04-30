from xmlrpc.client import TRANSPORT_ERROR
from django.contrib import admin

# Register your models here.
from crypto_app.models import *



admin.site.register(CryptoCurrency)
admin.site.register(Account)
admin.site.register(Transactions)

