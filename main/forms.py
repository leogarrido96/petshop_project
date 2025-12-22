from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    # Campo extra que não está no Model de mensagem, mas precisamos processar
    newsletter = forms.BooleanField(required=False, label="Desejo receber novidades")

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        # Widgets aplicam as classes CSS do Bootstrap
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
