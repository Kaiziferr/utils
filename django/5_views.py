# Vistas (views) --Logica/controlador
# This view is for view content
# **TemplateView**
```py
from django.views.generic import TemplateView

class <name_of_class>(TemplateView):
    
    template_name = '<name_of_template>' -- Indica donde esta el template.
```


# Vistas (views) --Logica/controlador
# This view is for list
# **PruebaListView**
```py
class ListarPruebaView(ListView):
    queryset # -- Podemos imprimir una lista
    model = Prueba #Aqui va el modelo Model
    template_name = 'home/prueba.html'
    context_object_name = 'lista_prueba' #Variable que accede al contexto de la lista en el template seria {{lista_prueba}}
```
