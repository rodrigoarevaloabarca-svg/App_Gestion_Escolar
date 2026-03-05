from django import forms
from alumnos.models import Alumno
from django.core.exceptions import ValidationError


class AlumnoForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'DD/MM/AAAA'}),
        input_formats=['%d/%m/%Y'],
        label="Fecha de Nacimiento"
    )
    class Meta:
        model = Alumno
        fields = ['rut', 'nombre', 'apellido', 'correo_electronico']
        labels = {
            'rut': 'RUT',
            'nombre' : 'Nombre',
            'correo_electronico': 'Correo Electronico'
        }
        widgets = {
            'rut': forms.TextInput(attrs={'placeholder': '12345678-9'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'correo_electronico': forms.EmailInput(attrs={'placeholder': 'Nombre@email.cl'})
        }

    def clean_rut(self):
        rut_raw = self.cleaned_data.get('rut', '').replace('.', '').replace('-', '').upper()

        if not rut_raw or len(rut_raw) < 2:
            raise ValidationError("El RUT es obligatorio.")

        cuerpo = rut_raw[:-1]
        dv = rut_raw[-1]

        if not cuerpo.isdigit():
            raise ValidationError("El RUT debe contener solo números antes del guion.")

        # Algoritmo de validación del dígito verificador
        suma = 0
        multiplicador = 2
        for i in reversed(cuerpo):
            suma += int(i) * multiplicador
            multiplicador = (multiplicador + 1) if multiplicador < 7 else 2

        dv_calculado = 11 - (suma % 11)
        dv_esperado = 'K' if dv_calculado == 10 else ('0' if dv_calculado == 11 else str(dv_calculado))

        if dv != dv_esperado:
            raise ValidationError("El RUT ingresado no es válido.")

        # Retornar formato estándar: 12.345.678-9
        return f"{int(cuerpo):,}".replace(',', '.') + f"-{dv}"