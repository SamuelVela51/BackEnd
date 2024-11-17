#app1/serializers.py

from rest_framework import serializers
from .models import Producto, Perfil, Categoria, Compra, CompraProducto


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'  

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    imagen_url = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'precio', 'stock', 'categoria', 'descripcion', 'imagen_url')

    def get_imagen_url(self, obj):
        request = self.context.get('request')
        # Primero verifica si la imagen existe y tiene un atributo 'url'
        if obj.imagen and hasattr(obj.imagen, 'url'):
            return request.build_absolute_uri(obj.imagen.url)
        return None  # Si no hay imagen, devuelve None



class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'


class CompraProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompraProducto
        fields = '__all__'

