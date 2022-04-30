# Generated by Django 4.0.4 on 2022-04-30 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crypto_app', '0013_alter_transaction_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='value',
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
