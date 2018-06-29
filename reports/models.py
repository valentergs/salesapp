from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()

from salesapp.models import SapBase

class Business(models.Model):
    unit = models.CharField(max_length=80)

    def __str__(self):
        return str(self.unit)
    
    class Meta:
        ordering            = ('unit',)
        verbose_name_plural = 'Business'

class Reports(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True, blank=True, null=True)
    author =        models.ForeignKey(User, related_name='reports', on_delete=models.CASCADE)
    customer =      models.ForeignKey(SapBase, related_name='reports', on_delete=models.CASCADE)
    subject =       models.CharField(max_length=250, blank=True, null=True)
    atendees =      models.CharField(max_length=250, blank=True, null=True)
    content =       models.TextField()
    status =        models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    business =      models.ManyToManyField(Business)

    def __str__(self):
        return str(self.customer)

    def get_absolute_url(self):
        return reverse('reports:details', kwargs={'username': self.author.username, 'pk': self.pk})

    class Meta:
        ordering =              ['-created_at']
        verbose_name_plural =   'Reports'
        unique_together =       ['author', 'content']
