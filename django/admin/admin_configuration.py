from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.


class EmpleadoAdmin(admin.ModelAdmin):

    list_display = (
        'first_name',
        'last_name',
        'department',
        'job'
    ) # lista los atributos que se quiere listar en el display

from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.


class EmpleadoAdmin(admin.ModelAdmin):

    list_display = (
        'first_name',
        'last_name',
        'department',
        'job'
    ) # lista los atributos que se quiere listar en el display

    search_fields = ('first_name', ) # Buscador
    list_filter = ('job', 'skills') # Ventana comporta como un filtro
    filter_horizontal = ('skills', ) # Filtro horizontal

admin.site.register(Empleado, EmpleadoAdmin)

admin.site.register(Habilidades)
