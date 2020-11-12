from django.urls import path
from .views import StockCreateView, StockListView,StockUpdateView,StockDeleteView, home, details

urlpatterns = [
    path('', home, name='home'),
    path('add/', StockCreateView.as_view(), name='add'),
    path('<int:pk>/update/', StockUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', StockDeleteView.as_view(), name='delete'),
    path('stock_list/', details, name='list'),
]