Instanciar el modelo
```py
from django.db import models

# Create your models here.
class PruebaHome(models.Model)


class Empleado(models.Model):
    """ Model para tabla Empleado """

    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )

    first_name = models.CharField('Nombres', max_length=60) 
    last_name = models.CharField('Apellido', max_length=60)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    
    class Meta:  # Modificar admin
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-first_name', 'last_name']
        unique_together = ('first_name', 'departamento')

    def __str__(self) -> str:
        return f'{self.id} - {self.first_name} - {self.last_name}'





```
