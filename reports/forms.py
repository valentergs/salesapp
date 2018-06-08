from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Reports, SapBase

class ReportsForm(forms.ModelForm):
    class Meta:
        exclude = ['created_at']
        model = Reports

    def __init__(self, user, *args, **kwargs):
        super(ReportsForm, self).__init__(*args, **kwargs)
        self.fields['customer'].queryset = SapBase.objects.filter(sellerNumber=self.request.user)