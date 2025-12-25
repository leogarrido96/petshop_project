from django.db import models
from django.contrib.auth.models import AbstractUser
from localflavor.br.validators import BRCPFValidator


class User(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF", null=True, blank=True, validators=[BRCPFValidator()])
    phone = models.CharField(max_length=20, verbose_name="Telefone", null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True, verbose_name="Foto de Perfil")

    def __str__(self):
        return self.username
