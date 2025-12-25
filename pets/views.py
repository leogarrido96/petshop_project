from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pet
from .forms import PetForm


class PetListView(LoginRequiredMixin, ListView):
    model = Pet
    template_name = 'pets/pet_list.html'
    context_object_name = 'my_pets'

    def get_queryset(self):
        # Garante que o usuário veja apenas os SEUS pets
        return Pet.objects.filter(owner=self.request.user)


class PetCreateView(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet_form.html'
    success_url = reverse_lazy('pet_list')

    def form_valid(self, form):
        # Vincula o pet automaticamente ao usuário logado
        form.instance = form.save(commit=False)
        form.instance.owner = self.request.user
        return super().form_valid(form)
