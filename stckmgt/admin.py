from django.contrib import admin
from .models import Stock
from .forms import AddItemForm

# Register your models here.

@admin.register(Stock)
class StockCreateAdmin(admin.ModelAdmin):
    form = AddItemForm
    list_display = ["item_no", "color", "quantity","issued_by"]
    search_fields = ["item_no", "color"] 
    list_filter = ["item_no", "color"]


# @admin.register(Stock)
# class ViewAdmin(admin.ModelAdmin):
#     pass
    


