# Generated by Django 2.0.2 on 2018-05-21 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesapp', '0002_auto_20180521_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='group',
        ),
    ]