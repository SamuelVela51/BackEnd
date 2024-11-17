from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings

# Tabla Perfil que extiende el modelo User
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return f'{self.usuario.username} Profile'


# Tabla Categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la categoria")

    def __str__(self):
        return self.nombre



class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del producto")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria", null=True, blank=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    descripcion = models.TextField(verbose_name="Descripción del producto", blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
    @property
    def imagen_url(self):
        if self.imagen:
            return settings.MEDIA_URL + str(self.imagen)
        return ''

# Tabla Compra
class Compra(models.Model):
    fecha = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario", null=True, blank=True)

    def __str__(self):
        return f'Compra {self.id} por {self.usuario.username}'


# Tabla intermedia para relacionar Compras y Productos
class CompraProducto(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'{self.cantidad} de {self.producto.nombre} en Compra {self.compra.id}'
