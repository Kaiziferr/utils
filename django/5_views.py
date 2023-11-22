# Vistas (views) --Logica/controlador
# This view is for view content
# **TemplateView**
```py
from django.views.generic import TemplateView

class <name_of_class>(TemplateView):
    
    template_name = '<name_of_template>' -- Indica donde esta el template.
```


class ListAllEmpleados(ListView):
    """Listar todos los empleados de una empresa"""
    template_name = 'empleado/list_empleados.html'
    model = Empleado
    context_object_name = 'lista_empleados'

class ListByAreaEmpleados(ListView):
    """Listar empleados de la empresa de un area"""
    template_name = 'empleado/list_empleado_area.html'

    def get_queryset(self) -> QuerySet[Any]:
        short_name = self.kwargs['short_name']        # Por medio del PATH
        queryset = Empleado.objects.filter(
            departamento__short_name = short_name
        )

        return queryset

class ListEmpleadosByKword(ListView):
    """ List of employers with a word"""

    template_name = 'empleado/by_kword.html'
    context_object_name = 'lista_empleados'

    def get_queryset(self) -> QuerySet[Any]:        # Por medio de un kword/form
        kword_kword = self.request.GET.get('kword', '')
        queryset = Empleado.objects.filter(
            first_name = kword_kword
        )
        return queryset
