from django import forms

from .models import Prueba

class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )

        widgets = {
            'titulo': forms.TextInput(
                attrs={# Atributos extra
                    'placeholder': 'Ingrese texto aqui'
                }
            )
        }

    # Validacion de campos
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un nùmero mayor o igual a 10')
        
        return cantidad


# -- Esto iria en la clase vista


from .form import PruebaForm
class PruebaCreateView(CreateView):
    template_name = 'home/add.html'
    model = Prueba
    form_class = PruebaForm
    success_url = reverse_lazy('home_app:correcto')

