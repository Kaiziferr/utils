class Meta:
    verbose_name = 'employee'
    verbose_name_plural = 'employees of enterprise'
    ordering = ['first_name', 'last_name'] # Criterios de orden
    unique_together = ('first_name', 'last_name') # No puede ingresar la misma combinación de valores dos veces.
