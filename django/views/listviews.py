```py
class PruebaListView(ListView):
  template_name = 'home/listar.html'
  queryset = ['A', 'B', 'C', 'D'] # queryset database
  context_object_name = 'lista_ejemplo'
```
