from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import ProductoForm, MarcaForm, CategoriaForm, ContenidoForm
from .models import Producto, Marca, Categoria, Contenido
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, 'stock/index.html')

class Productoview(ListView):
    model = Producto
    context_object_name = 'productos'

    def get_queryset(self):
        queryset = Producto.objects.all()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Producto.objects.filter(
                Q(nombre__icontains=busqueda) |
                Q(marca__nombre__icontains=busqueda) |
                Q(categoria__nombre__icontains=busqueda) |
                Q(precio__icontains=busqueda) |
                Q(contenido__nombre__icontains=busqueda) |
                Q(stock__icontains=busqueda)
            )
        return queryset

class ProductoDetail(DetailView):
    model = Producto

class ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class= ProductoForm
    success_url = reverse_lazy('stock:producto_list')

class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('stock:producto_list')

class ProductoCreate(LoginRequiredMixin, CreateView):
    model = Producto
    form_class= ProductoForm
    login_url = reverse_lazy('usuarios:login')
    success_url = reverse_lazy('stock:index')

class MarcaCreate(LoginRequiredMixin, CreateView):
    model = Marca
    form_class= MarcaForm
    success_url = reverse_lazy('stock:producto_form')

class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class= CategoriaForm
    success_url = reverse_lazy('stock:producto_form')

class ContenidoCreate(LoginRequiredMixin, CreateView):
    model = Contenido
    form_class= ContenidoForm
    success_url = reverse_lazy('stock:prodicto_form')

