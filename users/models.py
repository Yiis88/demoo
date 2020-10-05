from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UsuarioManager(BaseUserManager):
    def _create_user(self, email, nombres, apellidos, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            nombres=nombres,
            apellidos=apellidos,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, nombres, apellidos, password=None, **extra_fields):
        return self._create_user(email, nombres, apellidos, password, False, False, **extra_fields)

    def create_superuser(self, email, nombres, apellidos, password=None, **extra_fields):
        return self._create_user(email, nombres, apellidos, password, True, True, **extra_fields)


class Usuario(AbstractBaseUser):
    email = models.EmailField(primary_key=True, unique=True, blank=False,
                              null=False, max_length=255, verbose_name='Correo Electrónico')
    nombres = models.CharField(blank=True, null=True,
                               max_length=200, verbose_name='Nombres')
    apellidos = models.CharField(
        blank=True, null=True, max_length=200, verbose_name='Apellidos')

    imagen = models.ImageField(
        verbose_name='Imagen de Perfil', upload_to='perfil/', max_length=200, blank=True, null=True)

    is_active = models.BooleanField(default=True,
                                    verbose_name='¿Activo?')
    is_staff = models.BooleanField(
        default=False, verbose_name='¿Es Funcionario?')
    is_superuser = models.BooleanField(
        default=False, verbose_name='¿Es Administrador?')
    is_client = models.BooleanField(default=True, verbose_name='¿Es Cliente?')

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombres', 'apellidos']

    def tipo_usuario(self):
        if self.is_superuser:
            return "Administrador"
        if self.is_staff:
            return "Funcionario"
        if self.is_client:
            return "Cliente"
        return "Sin Información"

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        ordering = ['email']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
