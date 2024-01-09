```py
class PruebaListView(ListView):
  template_name = 'home/listar.html'
  queryset = ['A', 'B', 'C', 'D'] # queryset database
  context_object_name = 'lista_ejemplo'
```


```py
from django.shortcuts import render
from django.views.generic import ListView

from .models import Empleado
class ListAllEmpleados(ListView):
    template_name = 'empleado/listar_empleados.html'
    paginate_by = 4
    model = Empleado
    context_object_name = 'listar_empleado'
```

# Paginacion
# http://localhost:8000/listar-empleados/?page=2

```py
class ListByAreaEmpleados(ListView):
    """Listar empleados de la empresa de un area"""
    template_name = 'empleado/listar_empleado_area.html'
    def get_queryset(self) -> QuerySet[Any]:
        short_name = self.kwargs['short_name']
        queryset = Empleado.objects.filter(
            department__short_name = short_name
        )
        return queryset
```
# In url path('listar_empleado_area/<short_name>', views.ListByAreaEmpleados.as_view())

