from django import forms
from .models import Stock

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["category", "color", "quantity","opening_stck","issued_to" ,"phone_number","issued_by"]

    def clean_opening_stck(self):
        opening_stck = self.cleaned_data.get("opening_stck")
        if opening_stck < 0:
            raise forms.ValidationError("Data cannot be negative (-)")
        
        return opening_stck
      

    def clean_item_no(self):
        item_no = self.cleaned_data.get("item_no")
        if not item_no:
            raise forms.ValidationError('This field cannot be null')
        for instance in Stock.objects.all():
            if instance.item_no == item_no:
                raise forms.ValidationError(f'{item_no} is already in the DB')
        
        return item_no
        
    
    # def clean_color(self):
    #     color = self.cleaned_data("color")
    #     if not color:
    #         raise forms.ValidationError('This field cannot be null')
        
    #     return color


class SearchItemForm(forms.ModelForm):
    item_no = forms.CharField( max_length=50 , required=False)
    color = forms.CharField( max_length=50 , required=False)
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Stock
        fields = ["item_no", "color"]
