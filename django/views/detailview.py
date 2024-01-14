class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado/detalle_empleado.html' 

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Employee of the Month'
        return context
