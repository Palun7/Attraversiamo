from django.urls import path
from .views import (
    index,
    ProductoUpdate,
    ProductoDetail,
    ProductoCreate,
    ProductoDelete,
    Productoview,
    MarcaCreate,
    TalleCreate,
    CategoriaCreate
    )

app_name = 'stock'

urlpatterns = [
    path('stock/index', index, name='index'),
    path('stock/producto_list', Productoview.as_view(), name='producto_list'),
    path('stock/producto_create', ProductoCreate.as_view(), name='producto_create'),
    path('stock/producto_update/<int:pk>', ProductoUpdate.as_view(), name='producto_update'),
    path('stock/producto_detail/<int:pk>', ProductoDetail.as_view(), name='producto_detail'),
    path('stock/producto_delete/<int:pk>', ProductoDelete.as_view(), name='producto_delete'),
    path('stock/marca_create', MarcaCreate.as_view(), name='marca_create'),
    path('stock/talle_create', TalleCreate.as_view(), name='talle_create'),
    path('stock/categoria_create', CategoriaCreate.as_view(), name='categoria_create'),
]