from django.contrib import admin
from .models import *
from .forms import AddItemForm


@admin.register(Stock)
class StockCreateAdmin(admin.ModelAdmin):
    form = AddItemForm
    list_display = ["item_no", "color", "quantity","issued_by"]
    search_fields = ["item_no", "color"] 
    list_filter = ["item_no", "color"]


# admin.site.register(Category)
    


