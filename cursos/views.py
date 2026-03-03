from django.shortcuts import render
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def portal_cursos(request):
    return render(request, 'cursos/index.html')
@login_required
def lista_cursos(request):
    cursos = [
        "Lengua y Literatura", "Matemática", "Educación Ciudadana",
        "Ciencias para la Ciudadanía", "Historia, Geografía y Ciencias Sociales",
        "Inglés", "Filosofía", "Artes Visuales",
        "Educación Física y Salud", "Física"
    ]
    contexto = {"lista_cursos": cursos}
    return render(request,'cursos/lista_cursos.html', contexto)
@login_required
def registrar_curso(request):
    if request.method == 'GET':
        form = forms.CursosForm()
    else:
        form = forms.CursosForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data['codigo']
            nombre = form.cleaned_data['nombre_curso']
            contexto_post = {
                'codigo': codigo,
                'nombre': nombre
            }

            return render(request, 'cursos/exito.html', contexto_post)
    contexto = {'form': form}
    return render(request, 'cursos/agregar_cursos.html', contexto)