from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from users.models import Usuario


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('email', 'nombres', 'apellidos')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('email', 'nombres',
                  'apellidos', 'imagen', 'is_staff', 'is_client', 'is_superuser')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'nombres',
                    'apellidos',  'imagen', 'is_client', 'is_staff',  'is_superuser')
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {
         'fields': ('nombres', 'apellidos', 'imagen')}),
        ('Permisos', {
         'fields': ('is_client', 'is_staff',  'is_superuser',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombres', 'apellidos', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Usuario, UserAdmin)
admin.site.unregister(Group)

