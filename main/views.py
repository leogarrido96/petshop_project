from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import NewsletterSubscriber
from .forms import ContactForm

try:
    from catalog.models import Product
except ImportError:
    Product = None


class HomeView(TemplateView):
    """
    Renderiza a Home e busca os produtos de destaque.
    """
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Product:
            context['featured_products'] = Product.objects.filter(is_active=True)[:3]
        else:
            context['featured_products'] = []
        return context


class AboutView(TemplateView):
    """
    Exibe a página Sobre Nós.
    """
    template_name = 'main/about.html'


class ContactView(CreateView):
    """
    Exibe o formulário e salva a mensagem no banco automaticamente.
    """
    template_name = 'main/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')  # Redireciona para a mesma página após enviar

    def form_valid(self, form):
        newsletter = form.cleaned_data.get('newsletter')

        email = form.cleaned_data.get('email')

        # Só tenta salvar se o usuário marcou o checkbox E se existe um email
        if newsletter and email:
            NewsletterSubscriber.objects.get_or_create(email=email)

        # Adiciona mensagem de sucesso para aparecer no topo do site
        messages.success(self.request, 'Sua mensagem foi enviada com sucesso!')

        return super().form_valid(form)
