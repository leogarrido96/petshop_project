from django.views.generic import ListView
from .models import Category

class ProductListView(ListView):
    """
    Lista categorias e seus produtos vinculados.
    [cite_start]Reflete a página de produtos dividida em seções[cite: 27].
    """
    model = Category
    template_name = 'catalog/product_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        # Prefetch related otimiza a consulta ao banco (evita queries N+1)
        return Category.objects.prefetch_related('products').all()