from rest_framework import viewsets
from .models import Producto, Perfil, Categoria, Compra, CompraProducto
from .serializers import PerfilSerializer, CategoriaSerializer, ProductoSerializer, CompraSerializer, CompraProductoSerializer

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

class CompraProductoViewSet(viewsets.ModelViewSet):
    queryset = CompraProducto.objects.all()
    serializer_class = CompraProductoSerializer
