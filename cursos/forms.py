from django import forms

class CursosForm(forms.Form):
    # Si es del tipo TEXTO, debe ser CharField
    codigo = forms.CharField(label='Codigo', max_length=100)
    nombre_curso = forms.CharField(label='Nombre', max_length=100)