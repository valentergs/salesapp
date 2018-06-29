from django import forms
from django.http import request

from .models import Reports, SapBase

class ReportsForm(forms.ModelForm):
    class Meta:
        fields = ['customer', 'subject', 'atendees', 'content', 'status', 'business']
        model = Reports
        widgets = {'business': forms.CheckboxSelectMultiple}

    def __init__(self, user=None, *args, **kwargs):
        super(ReportsForm, self).__init__(*args, **kwargs)
        self.fields['customer'].queryset = SapBase.objects.filter(sellerNumber=user).order_by('soldToName').distinct('soldToName')
