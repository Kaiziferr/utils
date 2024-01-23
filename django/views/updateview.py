class EmpleadoUpdateView(UpdateView):
    template_name = 'empleado/update_empleado.html'
    model = Empleado
    fields = [
        'first_name', 
        'last_name',
        'job',
        'department',
        'skills']
    success_url = reverse_lazy('empleado_app:correcto') 
#path('actualizar-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar_empleado')
