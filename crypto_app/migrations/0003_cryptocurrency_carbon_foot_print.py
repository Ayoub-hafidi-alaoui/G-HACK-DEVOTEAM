# Generated by Django 4.0.4 on 2022-04-30 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_app', '0002_remove_cryptocurrency_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptocurrency',
            name='carbon_foot_print',
            field=models.FloatField(null=True),
        ),
    ]