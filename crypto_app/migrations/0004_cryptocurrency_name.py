# Generated by Django 4.0.4 on 2022-04-30 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_app', '0003_cryptocurrency_carbon_foot_print'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptocurrency',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]