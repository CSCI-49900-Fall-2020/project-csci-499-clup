# Generated by Django 3.1.3 on 2020-11-08 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20201108_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='store_capacity',
        ),
    ]
