# Generated by Django 4.0.4 on 2022-04-30 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_app', '0009_remove_cryptocurrency_created_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='user',
            new_name='transaction_user',
        ),
    ]