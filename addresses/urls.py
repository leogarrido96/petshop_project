from django.urls import path
from .views import AddressListView, AddressCreateView

urlpatterns = [
    path('meus-enderecos/', AddressListView.as_view(), name='address_list'),
    path('adicionar/', AddressCreateView.as_view(), name='address_add'),
]
