from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Photo
from .serializers import PhotoSerializer


class GalleryView(ListView):
    """
    [cite_start]Exibe todas as fotos cadastradas[cite: 30].
    """
    model = Photo
    template_name = 'gallery/gallery.html'
    context_object_name = 'photos'
    ordering = ['-uploaded_at']  # Fotos mais recentes primeiro


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API da Galeria de Fotos.
    Permite que o futuro App consuma as fotos dos pets.
    """
    queryset = Photo.objects.all().order_by('-uploaded_at')
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
