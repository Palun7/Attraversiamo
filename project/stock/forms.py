from django import forms
from .models import Producto, Marca, Categoria, Contenido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class ContenidoForm(forms.ModelForm):
    class Meta:
        model = Contenido
        fields = '__all__'