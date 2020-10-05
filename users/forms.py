from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Usuario
# Extendemos del original


class UsuarioCreateForm(UserCreationForm):
    # Ahora el campo username es de tipo email y cambiamos su texto
    email = forms.EmailField(label="Correo electrónico")
    nombres = forms.CharField(label='Nombres')
    apellidos = forms.CharField(label='Apellidos')

    class Meta:
        model = Usuario
        fields = ["email", "nombres", "apellidos", "password1", "password2"]
