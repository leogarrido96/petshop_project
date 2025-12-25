from django.contrib.auth.forms import UserCreationForm
from localflavor.br.forms import BRCPFField
from .models import User


class CustomUserCreationForm(UserCreationForm):
    cpf = BRCPFField(label="CPF", help_text="Formato: 000.000.000-00")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            'first_name',
            'last_name',
            'email',
            'cpf',
            'phone',
            'profile_picture',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'profile_picture':
                field.widget.attrs.update({'class': 'form-control-file'})
            else:
                field.widget.attrs.update({'class': 'form-control'})
