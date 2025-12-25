from django.db import models
from django.conf import settings


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='addresses')
    zip_code = models.CharField(max_length=9, verbose_name="CEP")
    street = models.CharField(max_length=255, verbose_name="Logradouro")
    number = models.CharField(max_length=10, verbose_name="Número")
    complement = models.CharField(max_length=100, blank=True, verbose_name="Complemento")
    neighborhood = models.CharField(max_length=100, verbose_name="Bairro")
    city = models.CharField(max_length=100, default="Salvador", verbose_name="Cidade")
    state = models.CharField(max_length=2, default="BA", verbose_name="Estado")
    is_main = models.BooleanField(default=False, verbose_name="Endereço Principal")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return f"{self.street}, {self.number} - {self.neighborhood}, {self.city} - {self.state}"
