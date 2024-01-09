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
