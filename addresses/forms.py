from django import forms
from .models import Address
from localflavor.br.forms import BRStateSelect


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['zip_code', 'street', 'number', 'complement', 'neighborhood', 'city', 'state', 'is_main']
        widgets = {
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00000-000'}),
            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rua Exemplo'}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123'}),
            'neighborhood': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro Exemplo'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade Exemplo'}),
            'state': BRStateSelect(attrs={'class': 'form-select'}),
            'complement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apto, Bloco, etc. (opcional)'}),
        }
