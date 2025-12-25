from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome da Categoria")
    slug = models.SlugField(unique=True, help_text="Identificador único para URL (ex: ração-premium)")
    description = models.TextField(verbose_name="Descrição da Categoria", blank=True, null=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Categoria")
    name = models.CharField(max_length=200, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Preço (R$)")
    promotional_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Preço Promocional (R$)")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantidade em Estoque")
    image = models.ImageField(upload_to='products/', verbose_name="Imagem")
    is_active = models.BooleanField(default=True, verbose_name="Ativo?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Produto/Serviço"
        verbose_name_plural = "Produtos e Serviços"

    def __str__(self):
        return self.name
