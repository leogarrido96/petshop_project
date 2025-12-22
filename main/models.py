from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="E-mail")
    phone = models.CharField(max_length=20, verbose_name="Telefone")
    message = models.TextField(verbose_name="Mensagem")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Enviado em")
    is_read = models.BooleanField(default=False, verbose_name="Lido?")

    class Meta:
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%d/%m/%Y')}"

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name="E-mail")
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name="Inscrito em")

    class Meta:
        verbose_name = "Inscrito na Newsletter"
        verbose_name_plural = "Inscritos na Newsletter"

    def __str__(self):
        return self.email
    

class SiteConfiguration(models.Model):
    # Imagens da Home
    home_banner = models.ImageField(upload_to='site_setup/', verbose_name="Banner da Página Inicial")
    
    # Imagens do Sobre Nós
    about_image = models.ImageField(upload_to='site_setup/', verbose_name="Foto da Seção Sobre Nós")
    
    # Imagens do Contato (Opcional)
    contact_banner = models.ImageField(upload_to='site_setup/', blank=True, null=True, verbose_name="Banner da Página de Contato")

    class Meta:
        verbose_name = "Configuração do Site"
        verbose_name_plural = "Configurações do Site"

    def __str__(self):
        return "Configuração Principal (Edite aqui)"