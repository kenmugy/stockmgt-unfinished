from django import forms
from .models import Stock

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['item_no', 'color', 'quantity', 'issued_by']
