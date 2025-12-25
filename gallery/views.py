from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Photo
from .serializers import PhotoSerializer
from .forms import PhotoUploadForm


class GalleryView(ListView):
    model = Photo
    template_name = 'gallery/gallery.html'
    context_object_name = 'photos'

    def get_queryset(self):
        """
        Retorna apenas as fotos aprovadas (active=True) para o público geral.
        """
        return Photo.objects.filter(active=True).order_by('-uploaded_at')

    def get_context_data(self, **kwargs):
        """
        Adiciona as fotos pendentes ao contexto,
        mas apenas se o usuário for da equipe (admin/staff).
        """
        context = super().get_context_data(**kwargs)

        if self.request.user.is_staff:
            context['photos_to_validate'] = Photo.objects.filter(
                active__isnull=True
            ).order_by('-uploaded_at')

        return context


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API da Galeria de Fotos.
    Permite que o futuro App consuma as fotos dos pets.
    """
    queryset = Photo.objects.all().order_by('-uploaded_at')
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoUploadForm
    template_name = 'gallery/photo_form.html'
    success_url = reverse_lazy('gallery:gallery_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.active = None
        return super().form_valid(form)


@staff_member_required
def photo_action(request, pk, action):
    photo = get_object_or_404(Photo, pk=pk)

    if action == 'approve':
        photo.active = True
    elif action == 'reject':
        photo.active = False

    photo.save()
    return redirect('gallery:gallery_list')
