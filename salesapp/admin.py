from django.contrib import admin
from salesapp.models import Customers

class CustomersAdmin(admin.ModelAdmin):
    list_display = ['soldToName', 'sellerName']
    list_filter = ['sellerName', 'products']

admin.site.register(Customers, CustomersAdmin)
