from django.shortcuts import render
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def portal_alumnos(request):
    return render(request, 'alumnos/index.html')
@login_required
def lista_alumnos(request):
    alumnos = [
        "Matías Iturra", "Valentina Rojas", "Benjamín Soto",
        "Catalina Fuenzalida", "Nicolás Mardones", "Isidora Pizarro",
        "Sebastián Caviedes", "Florencia Araya", "Diego Poblete", "Antonia Lagos"
    ]
    contexto = {"lista_alumnos": alumnos}
    return render(request,'alumnos/lista_alumnos.html', contexto)
@login_required
def registrar_alumno(request):
    if request.method == 'GET':
        form = forms.AlumnoForm()
    else:
        form = forms.AlumnoForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['correo_electronico']
            contexto_post = {
                'rut': rut,
                'nombre': nombre,
                'apellido': apellido,
                'email': email
            }

            return render(request, 'alumnos/exito.html', contexto_post)
    contexto = {'form': form}
    return render(request, 'alumnos/agregar_alumno.html', contexto)