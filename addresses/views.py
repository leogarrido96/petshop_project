from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Address
from .forms import AddressForm


class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'addresses/address_list.html'
    context_object_name = 'my_addresses'

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)


class AddressCreateView(LoginRequiredMixin, CreateView):
    model = Address
    form_class = AddressForm
    template_name = 'addresses/address_form.html'
    success_url = reverse_lazy('address_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
