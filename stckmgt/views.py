from django.shortcuts import render
from django.views.generic import CreateView
from .models import Stock

# Create your views here.

class StockCreateView(CreateView):
    model = Stock
    fields = ['item_no', 'color', 'quantity', 'opening_stck']
    
