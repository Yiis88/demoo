from django.contrib import admin
from users.models import Usuario
from .models import Departamento, TipoServicioExtra, Reserva, DetalleServicio 
from .models import Elemento, Inventario, TipoMantencion, Mantencion, Agenda, CheckList, CheckIn, CheckOut



# Register your models here.

admin.site.register(Departamento)
admin.site.register(TipoServicioExtra)
admin.site.register(Reserva)
admin.site.register(DetalleServicio)
admin.site.register(Elemento)
admin.site.register(Inventario)
admin.site.register(TipoMantencion)
admin.site.register(Mantencion)
admin.site.register(Agenda)
admin.site.register(CheckList)
admin.site.register(CheckIn)
admin.site.register(CheckOut)
