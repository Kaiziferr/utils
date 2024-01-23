
class RegistroEmpleado(CreateView):
    model = Empleado
    template_name = 'empleado/register_empleado.html'
    #fields = ['first_name', 'last_name']
    fields = ('__all__')
    success_url = '.' # recharge the same page
    
# Template {{form.as_p}}

class RegistroEmpleado(CreateView):
    model = Empleado
    template_name = 'empleado/register_empleado.html'
    fields = [
        'first_name', 
        'last_name',
        'job',
        'department',
        'skills']
    #fields = ('__all__')
    success_url = reverse_lazy('empleado_app:correcto') # recharge the same page

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        empleado = form.save(commit=False) # Almacene todos los valores en la base de datos
        empleado.full_name = f'{empleado.first_name} {empleado.last_name}'
        empleado.save()
        return super(RegistroEmpleado, self).form_valid(form)
