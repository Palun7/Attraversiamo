from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import PasswordChangeForm


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model= User
        fields = ['username', 'password']

class CustomUserCreationForm(UserCreationForm):
    OPCIONES = [
        ('vendedor', 'vendedor'),
        ('deposito', 'deposito'),
        ('repositor', 'repositor'),
    ]
    nombre = forms.CharField(max_length=30, required=True, help_text='Obligatorio')
    apellido = forms.CharField(max_length=30, required=True, help_text='Obligatorio')
    mail = forms.EmailField(max_length=50, required=True, help_text='Obligatorio. Coloque un mail válido')
    puesto = forms.ChoiceField(choices=OPCIONES, required=True, help_text='seleccione una opción')

    class Meta:
        model = User
        fields = ['nombre', 'apellido', 'username', 'mail', 'puesto', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.nombre = self.cleaned_data['nombre']
        user.apellido = self.cleaned_data['apellido']
        user.mail = self.cleaned_data['mail']
        user.puesto = self.cleaned_data['puesto']
        if commit:
            user.save()
        return user

class UpdateUsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

    def __init__(self, *args, **kwargs):
        super(UpdateUsernameForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})