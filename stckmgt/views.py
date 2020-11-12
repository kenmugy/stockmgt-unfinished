from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Stock


class StockCreateView(CreateView):
    model = Stock
    fields = ['item_no', 'color', 'quantity', 'opening_stck']

class StockListView(ListView):
    model = Stock
    ordering = '-last_updated'
    template_name = 'stckmgt/stock_detail.html'
    context_object_name = 'items'
