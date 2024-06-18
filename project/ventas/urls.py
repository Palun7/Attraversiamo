from django.urls import path
from .views import index

app_name = 'ventas'

urlpatterns = [
    path('ventas/', index, name='index')
]