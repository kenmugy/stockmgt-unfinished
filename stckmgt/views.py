from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.messages import info
from .models import Stock
from .forms import SearchItemForm

from django.http import HttpResponse
import csv

class StockCreateView(CreateView):
    model = Stock
    fields = ['item_no', 'color', 'quantity', 'opening_stck']

class StockListView(ListView):
    model = Stock
    ordering = '-last_updated'
    context_object_name = 'items'

    

class StockUpdateView(UpdateView):
    model = Stock
    fields = ["opening_stck"]

class StockDeleteView(DeleteView):
    model = Stock
    success_url = 'stock_list/'

class StockDetailView(DetailView):
    model = Stock


def home(request):
    return render(request, 'stckmgt/home.html')
    
def details(request):
    form = SearchItemForm(request.POST or None)
    items = Stock.objects.all().order_by('-last_updated')
    context = {'form': form, 'items': items}
    if form.is_valid():
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['ITEM NO', 'STOCK COLOR', 'QUANTITY'])
            instance = items
            for stock in instance:
                writer.writerow([stock.item_no, stock.color, stock.quantity])
            return response
        query_set = Stock.objects.filter(item_no__icontains = form['item_no'].value(), color__icontains = form['color'].value())
        context = {'form': form, 'items': query_set}

    return render(request, 'stckmgt/stock_list.html', context)
    
    