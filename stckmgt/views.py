from django.shortcuts import render
from django.views.generic import CreateView
from .models import Stock

# Create your views here.

class StockCreateView(CreateView):
    model = Stock
    template_name = "stckmgt/add_item.html"
