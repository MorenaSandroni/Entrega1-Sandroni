from django.shortcuts import render
from app.forms import formProfesores, formEstudiantes,formMaestranza
from app.models import Profesor, Estudiante, Maestranza


# Create your views here.

def formProfesores(request):

    if request.method == 'POST':
        formProf = formProfesores(request.POST)

        if formProf.is_valid:
            data = formProf.cleaned_data
            profesor = Profesor (nombre = data["nombre"], apellido = data["apellido"], dni = data["dni"], asignatura = data["asignatura"])
            profesor.save()
            return render (request, "app/profesores.html")
    else:
        formProf = formProfesores()
        return render (request, "app/profesores.html",{"formProf":formProf})