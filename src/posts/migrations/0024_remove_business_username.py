# Generated by Django 3.1.2 on 2020-10-18 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_auto_20201018_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='username',
        ),
    ]
