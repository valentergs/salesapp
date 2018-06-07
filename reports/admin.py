from django.contrib import admin
from reports.models import Reports, Business

class ReportsAdmin(admin.ModelAdmin):
    list_filter = ['status', 'author', 'created_at']
    list_display = ['customer', 'created_at', 'author']

admin.site.register(Reports, ReportsAdmin)
admin.site.register(Business)