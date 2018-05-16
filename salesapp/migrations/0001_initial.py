# Generated by Django 2.0.2 on 2018-05-16 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soldToNumber', models.IntegerField()),
                ('soldToName', models.CharField(max_length=80)),
                ('shipToNumber', models.IntegerField()),
                ('shipToName', models.CharField(max_length=80)),
                ('shipToCity', models.CharField(max_length=80)),
                ('shipToCountry', models.CharField(max_length=80)),
                ('products', models.CharField(max_length=80)),
                ('sellerNumber', models.IntegerField()),
                ('sellerName', models.CharField(max_length=80)),
                ('cmscNumber', models.IntegerField()),
                ('cmscName', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Customers',
            },
        ),
    ]
