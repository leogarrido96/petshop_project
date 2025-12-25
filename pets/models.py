from django.db import models
from django.conf import settings


class Pet(models.Model):
    SPECIES_CHOICES = [
        ('dog', 'Cão'),
        ('cat', 'Gato'),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField(max_length=100, verbose_name="Nome do Pet")
    species = models.CharField(max_length=10, choices=SPECIES_CHOICES, verbose_name="Espécie")
    breed = models.CharField(max_length=100, blank=True, verbose_name="Raça")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")

    observations = models.TextField(blank=True, verbose_name="Observações de Saúde/Comportamento")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pet"
        verbose_name_plural = "Pets"

    def __str__(self):
        return f"{self.name} ({self.get_species_display()})"
