from django.urls import path
from .views import StockCreateView

urlpatterns = [
    path('add', StockCreateView, name='add'),
]