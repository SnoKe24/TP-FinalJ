from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    nombre = forms.CharField(
        label="Nombre",
        max_length=50,
        widget=forms.TextInput(attrs={"class":"form-control"})
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="Repetir contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    class Meta:
        model = Usuario
        fields = ("nombre","email", "rol")
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "rol": forms.Select(attrs={"class": "form-select"}),
        }


class LoginEmailForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Ingresa tu email"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Contraseña"
    }))