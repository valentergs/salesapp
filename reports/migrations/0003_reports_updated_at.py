# Generated by Django 2.0.2 on 2018-06-29 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20180626_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='updated_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
