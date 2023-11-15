
# Modificar admin desde la clase models

# Create your models here.
class Empleado(models.Model):
    """ Model para tabla Empleado """
    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-first_name', 'last_name']
        unique_together = ('first_name', 'departamento')

clase admin   
from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Habilidades)

# Modifica la vista del administrador para la clase Empleado 
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name' #New columns, no is in the model
    )

    def full_name(self, obj):# return values for new columns
        print(obj) # loop all rows of models 
        return f'{obj.first_name} {obj.last_name}'

    search_fields = ('first_name', ) # Filtro buscar en el admin
    list_filter = ('job', 'habilidades') # Filtro en forma de lista
    filter_horizontal = ('habilidades', )

admin.site.register(models.Empleado, EmpleadoAdmin)
