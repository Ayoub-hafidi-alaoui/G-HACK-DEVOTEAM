# Generated by Django 4.0.4 on 2022-04-30 10:15

from django.db import migrations, models
import django.template.defaulttags


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_app', '0006_cryptocurrency_updated_alter_cryptocurrency_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cryptocurrency',
            name='updated',
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='created',
            field=models.DateTimeField(default=django.template.defaulttags.now),
        ),
    ]
