from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nome do Pet / Título")
    caption = models.CharField(max_length=255, blank=True, verbose_name="Legenda")
    image = models.ImageField(upload_to='gallery/', verbose_name="Foto")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Galeria de Fotos"
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title