from django import forms
from .models import Stock

class AddItem(forms.ModelForm):
    class Meta:
        model = Stock
