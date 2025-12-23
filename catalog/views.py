from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer


class ProductListView(ListView):
    """
    Lista categorias e seus produtos vinculados.
    """
    model = Category
    template_name = 'catalog/product_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.prefetch_related('products').all()


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API para listar as categorias do petshop.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    """
    API para gerenciar os produtos e serviços ofertados.
    """
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
