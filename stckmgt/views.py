from django.shortcuts import render
from django.views.generic import CreateView
from .models import Stock
# from .forms import AddItem

# Create your views here.

class StockCreateView(CreateView):
    model = Stock
    # template_name = 'stckmgt/stock_form.html'
    fields = ['item_no', 'color', 'quantity', 'opening_stck']

# def add_item(request):
#     form = AddItem(request.POST | None)
#     return render(request, 'stckmgt/stock_form.html', {'form': form})
