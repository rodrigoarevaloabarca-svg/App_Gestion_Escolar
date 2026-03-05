from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from alumnos.models import Alumno
from alumnos.forms import AlumnoForm
# Create your views here.
@login_required
def portal_alumnos(request):
    return render(request, 'alumnos/index.html')
@login_required
def lista_alumnos(request):
    # Acá se ejecuta un "SELECT * FROM alumnos_alumno"
    alumnos = Alumno.objects.all()
    contexto = {'lista_alumnos': alumnos}
    return render(request, 'alumnos/lista_alumnos.html', contexto)

@login_required
def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
        contexto = {'form': form}
    return render(request, 'alumnos/agregar_alumno.html', contexto)