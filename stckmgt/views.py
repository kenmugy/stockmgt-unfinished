from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.messages import info
from .models import Stock
from .forms import SearchItemForm


class StockCreateView(CreateView):
    model = Stock
    fields = ['item_no', 'color', 'quantity', 'opening_stck']

class StockListView(ListView):
    model = Stock
    ordering = '-last_updated'
    template_name = 'stckmgt/stock_detail.html'
    context_object_name = 'items'

class StockUpdateView(UpdateView):
    model = Stock
    fields = ["opening_stck"]


def home(request):
    return render(request, 'stckmgt/home.html')
    
def details(request):
    form = SearchItemForm(request.POST or None)
    items = Stock.objects.all().order_by('-last_updated')
    context = {'form': form, 'items': items}
    if form.is_valid():
        query_set = Stock.objects.filter(item_no__icontains = form['item_no'].value(), color__icontains = form['color'].value())
        context = {'form': form, 'items': query_set}

    return render(request, 'stckmgt/stock_detail.html', context)
    
    