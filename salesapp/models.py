from django.db import models

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

    def __str__(self):
        return self.soldToName

    class Meta:
        verbose_name_plural = 'Customers'
