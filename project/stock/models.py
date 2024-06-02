from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

class Contenido(models.Model):
    numero = models.CharField(max_length=10)
    unidad_medida = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.numero} {self.unidad_medida}'

    class Meta:
        verbose_name = 'Contenido'
        verbose_name_plural = 'Contenidos'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey('Marca', on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=True)
    precio = models.FloatField()
    contenido = models.ForeignKey('Contenido', on_delete=models.SET_NULL, null=True, blank=True)
    stock = models.PositiveIntegerField()
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)
    actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f'{self.nombre} {self.marca} {self.contenido}. Act: {self.actualizacion.day}/{self.actualizacion.month}/{self.actualizacion.year}'