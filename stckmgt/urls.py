from django.urls import path
from .views import StockCreateView

urlpatterns = [
    path('add/', StockCreateView.as_view(), name='add'),
    # path('add/', StockCreateView, name='add'),
]