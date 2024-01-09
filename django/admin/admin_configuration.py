from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.


class EmpleadoAdmin(admin.ModelAdmin):

    list_display = (
        'first_name',
        'last_name',
        'department',
        'job',
        'full_name' # Valor compuesto
    ) # lista los atributos que se quiere listar en el display

    def full_name(self, obj): # Debe tener el mismo nombre
        fname = f'{obj.first_name} {obj.last_name}'
        return fname

    search_fields = ('first_name', ) # Buscador
    list_filter = ('job', 'skills') # Ventana comporta como un filtro
    filter_horizontal = ('skills', ) # Filtro horizontal

admin.site.register(Empleado, EmpleadoAdmin)

admin.site.register(Habilidades)
