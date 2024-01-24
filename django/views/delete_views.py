
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleado/delete_empleado.html'
    success_url = reverse_lazy('empleado_app:correcto')

# Requiere un form
<h1>ELiminar empleado </h1>

<form method="POST"> {% csrf_token %}
    <p>Confirmar</p>
    <button type="submit">Confirmar</button>
</form>
