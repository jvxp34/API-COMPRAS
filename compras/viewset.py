from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Usuario, Product, ListaCompra, Item
from .serializers import (
    UsuarioSerializer,
    ProductSerializer,
    ListaCompraSerializer,
    ItemSerializer
)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ListaCompraViewSet(viewsets.ModelViewSet):
    queryset = ListaCompra.objects.all()
    serializer_class = ListaCompraSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ['usuario']
    search_fields = ['nome']
    ordering_fields = ['data_criacao', 'total']

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ['lista', 'comprado', 'product']
    search_fields = ['product__nome']
    ordering_fields = ['valor', 'data_criacao']