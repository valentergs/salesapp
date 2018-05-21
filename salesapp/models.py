from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Groups(models.Model):
    group = models.CharField(max_length=100)

class Customers(models.Model):
    soldToNumber = models.CharField(max_length=10)
    soldToName = models.CharField(max_length=80)
    shipToNumber = models.CharField(max_length=10)
    shipToName = models.CharField(max_length=80)
    shipToCity = models.CharField(max_length=80)
    shipToCountry = models.CharField(max_length=80)
    products = models.CharField(max_length=80)
    sellerNumber = models.CharField(max_length=10)
    sellerName = models.CharField(max_length=80)
    cmscNumber = models.CharField(max_length=10)
    cmscName = models.CharField(max_length=80)

    def get_absolute_url(self):
        return reverse('url_cust_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.soldToName

    class Meta:
        verbose_name_plural = 'Customers'

