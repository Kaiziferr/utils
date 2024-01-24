
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleado/delete_empleado.html'
    success_url = reverse_lazy('empleado_app:correcto')
