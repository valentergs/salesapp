from django.forms import ModelForm
from django import forms
from reports import models

class ReportsForm(forms.ModelForm):
    class Meta:
        fields = ('author', 'customer', 'content', 'status', 'business',)
        model = models.Reports
        # widgets = {'visit_date': forms.DateInput()}
        widgets = {'visit_date': forms.SelectDateWidget(),
                    'business': forms.MultipleChoiceField(),
        }