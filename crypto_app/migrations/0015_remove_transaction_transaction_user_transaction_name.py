# Generated by Django 4.0.4 on 2022-04-30 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_app', '0014_remove_transaction_value_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_user',
        ),
        migrations.AddField(
            model_name='transaction',
            name='name',
            field=models.FloatField(max_length=30, null=True),
        ),
    ]