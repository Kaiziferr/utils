class SuccessView(TemplateView):
    template_name = 'empleado/success.html'

class RegistroEmpleado(CreateView):
    model = Empleado
    template_name = 'empleado/register_empleado.html'
    #fields = ['first_name', 'last_name']
    fields = ('__all__')
    success_url = reverse_lazy('success/') # recharge the same page
# La idea es que redireccione, cuando se ejecute el proceso.
