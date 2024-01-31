# Create your views here.
from django.views.generic.edit import (
    FormView
)
from .forms import NewDepartamentForm # -- Este es el formulario

from .models import Departamento
from applications.empleado.models import Empleado



class NewDepartament(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class =  NewDepartamentForm
    success_url = '/'

    def form_valid(self, form) -> HttpResponse:
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        departamento = form.cleaned_data['departamento']
        short_name = form.cleaned_data['short_name']
        
        departament = Departamento(
            name = departamento,
            short_name = short_name
        )

        departament.save()

        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            department = departament
        )


        return super(NewDepartament, self).form_valid(form)
    
