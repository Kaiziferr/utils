
class RegistroEmpleado(CreateView):
    model = Empleado
    template_name = 'empleado/register_empleado.html'
    #fields = ['first_name', 'last_name']
    fields = ('__all__')
    success_url = '.' # recharge the same page
    
# Template {{form.as_p}}
