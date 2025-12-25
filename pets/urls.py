from django.urls import path
from .views import PetListView, PetCreateView

urlpatterns = [
    path('meus-pets/', PetListView.as_view(), name='pet_list'),
    path('cadastrar/', PetCreateView.as_view(), name='pet_add'),
]
