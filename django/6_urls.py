# as_view() Se usa con vistas genericas.

# Manda un parametro por la url
path('listar_empleado_area/<short_name>', views.ListByAreaEmpleados.as_view())
