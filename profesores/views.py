from django.shortcuts import render
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def portal_profesores(request):
    return render(request, 'profesores/index.html')
@login_required
def lista_profesores(request):
    profesores = [
        "Ricardo Yáñez", "Patricia Henríquez", "Sergio Villalobos",
        "Mónica Espinoza", "Andrés Sanhueza", "Loreto Valenzuela",
        "Cristian Farías", "Gloria Maturana", "Hugo Saavedra", "Carmen Gloria Palma"
    ]
    contexto = {"lista_profesores": profesores}
    return render(request,'profesores/lista_profesores.html', contexto)
@login_required
def registrar_profesor(request):
    if request.method == 'GET':
        form = forms.ProfesorForm()
    else:
        form = forms.ProfesorForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            especialidad = form.cleaned_data['especialidad']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['correo_electronico']
            contexto_post = {
                'rut': rut,
                'nombre': nombre,
                'apellido': apellido,
                'especialidad': especialidad,
                'telefono': telefono,
                'email': email
            }
            return render(request, 'profesores/exito.html', contexto_post)

    contexto = {'form': form}
    return render(request, 'profesores/agregar_profesor.html',contexto)