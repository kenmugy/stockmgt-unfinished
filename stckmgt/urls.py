from django.urls import path
from .views import StockCreateView, StockListView, home

urlpatterns = [
    path('', home, name='home'),
    path('add/', StockCreateView.as_view(), name='add'),
    path('stock_list/', StockListView.as_view(), name='details'),
]