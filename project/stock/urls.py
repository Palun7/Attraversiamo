from django.urls import path
from .views import index

app_name = 'stock'

urlpatterns = [
    path('stock/index', index, name='index')
]