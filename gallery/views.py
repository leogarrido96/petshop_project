from django.views.generic import ListView
from .models import Photo


class GalleryView(ListView):
    """
    [cite_start]Exibe todas as fotos cadastradas[cite: 30].
    """
    model = Photo
    template_name = 'gallery/gallery.html'
    context_object_name = 'photos'
    ordering = ['-uploaded_at']  # Fotos mais recentes primeiro
