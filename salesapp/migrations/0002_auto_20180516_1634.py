# Generated by Django 2.0.2 on 2018-05-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='cmscNumber',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customers',
            name='sellerNumber',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customers',
            name='shipToNumber',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customers',
            name='soldToNumber',
            field=models.CharField(max_length=10),
        ),
    ]
