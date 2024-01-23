# El proceso de reverso de una redirecciòn

class SuccessView(TemplateView):
    template_name = 'empleado/success.html'

class RegistroEmpleado(CreateView):
    model = Empleado
    template_name = 'empleado/register_empleado.html'
    #fields = ['first_name', 'last_name']
    fields = ('__all__')
    success_url = reverse_lazy('empleado_app:correcto') # recharge the same page
from django.urls import path, include

from . import views

app_name = 'empleado_app' # Name of the app

urlpatterns = [
    ...
    path('success/', views.SuccessView.as_view(), name='correcto')
]

