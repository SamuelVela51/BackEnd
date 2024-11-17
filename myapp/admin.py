from django.contrib import admin
from .models import Perfil, Categoria, Producto, Compra, CompraProducto

# Register your models here.


admin.site.register(Perfil)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(CompraProducto)

