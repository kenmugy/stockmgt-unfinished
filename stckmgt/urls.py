from django.urls import path
from .views import StockCreateView, StockListView

urlpatterns = [
    path('add/', StockCreateView.as_view(), name='add'),
    path('stock_list/', StockListView.as_view(), name='details'),
]