# Generated by Django 4.0.4 on 2022-04-30 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_app', '0006_account_cryptocurrency_account_solde_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptocurrency',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='cryptocurrency',
            name='update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
