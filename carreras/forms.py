from django import forms


class CarreraForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre', 
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese nombre de la carrera',
                'class': 'form-control w-50'
            }
        )
    )
    duracion = forms.IntegerField(
        label='Duracion', 
        min_value=1, 
        max_value=5, 
        required=True,
         widget=forms.TextInput(
            attrs={
                'placeholder': 'Duracion',
                'class': 'form-control w-50'
            }
        )
    )