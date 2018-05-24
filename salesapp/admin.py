from django.contrib import admin
from salesapp.models import Customers, Groups

class CustomersAdmin(admin.ModelAdmin):
    list_display = ['soldToName', 'sellerName']
    list_filter = ['sellerName', 'products', 'soldToName']

admin.site.register(Customers, CustomersAdmin)
admin.site.register(Groups)

