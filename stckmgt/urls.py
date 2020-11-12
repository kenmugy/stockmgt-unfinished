from django.urls import path
from .views import StockCreateView, StockListView,StockUpdateView, home, details

urlpatterns = [
    path('', home, name='home'),
    path('add/', StockCreateView.as_view(), name='add'),
    path('update/<int:pk>', StockUpdateView.as_view(), name='update'),
    # path('stock_list/', StockListView.as_view(), name='details'),
    path('stock_list/', details, name='details'),
]