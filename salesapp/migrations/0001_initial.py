# Generated by Django 2.0.2 on 2018-05-28 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='SapBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soldToNumber', models.CharField(max_length=10)),
                ('soldToName', models.CharField(max_length=80)),
                ('shipToNumber', models.CharField(max_length=10)),
                ('shipToName', models.CharField(max_length=80)),
                ('shipToCity', models.CharField(max_length=80)),
                ('shipToCountry', models.CharField(max_length=80)),
                ('products', models.CharField(max_length=80)),
                ('sellerNumber', models.CharField(max_length=10)),
                ('sellerName', models.CharField(max_length=80)),
                ('cmscNumber', models.CharField(max_length=10)),
                ('cmscName', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('sapbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='salesapp.SapBase')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked'), ('delete', 'Delete')], default='active', max_length=10)),
                ('is_dist', models.BooleanField(default=False)),
                ('group', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='salesapp.Groups')),
            ],
            bases=('salesapp.sapbase',),
        ),
    ]
