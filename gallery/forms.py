from django import forms
from .models import Photo


class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image', 'caption']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do seu Pet'}),
            'caption': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Conte algo sobre ele...'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
