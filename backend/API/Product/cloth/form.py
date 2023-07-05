from django import forms
from .models import sales


class SaleForm(forms.ModelForm):
    class Meta:
        model = sales
        fields = ['name','description', 'price', 'category']
        