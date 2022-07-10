from django.shortcuts import render
from app.forms import  formProfesores, formEstudiantes,formMaestranza, form_busqueda_estudiantes
from app.models import Profesor, Estudiante, Maestranza


# Create your views here.
def index(request):
    return render (request, "app/index.html", {})

def form_Profesores(request):

    if request.method == 'POST':
        formProf = formProfesores(request.POST)

        if formProf.is_valid():
            informacion = formProf.cleaned_data
            profesor = Profesor (nombre = informacion["nombre"], apellido = informacion["apellido"], dni = informacion["dni"], asignatura = informacion["asignatura"])
            profesor.save()
            chequeo = print ("Se ha registrado con exito el formulario. Muchas Gracias")
            return render (request, "app/profesores.html")
    else:
        formProf = formProfesores()
        return render (request, "app/profesores.html",{"formProf":formProf})


def form_Estudiantes(request):

    if request.method == 'POST':
        formEstu = formEstudiantes(request.POST)

        if formEstu.is_valid():
            data = formEstu.cleaned_data
            estudiante = Estudiante (nombre = data["nombre"], apellido = data["apellido"], dni = data["dni"], curso = data["curso"])
            estudiante.save()
            chequeo = print ("Se ha registrado con exito el formulario. Muchas Gracias")
            return render (request, "app/estudiantes.html")
    else:
        formEstu = formEstudiantes()
        return render (request, "app/estudiantes.html",{"formEstu":formEstu})



def form_Maestranza(request):

    if request.method == 'POST':
        formMaes = formMaestranza(request.POST)

        if  formMaes.is_valid():
            data =  formMaes.cleaned_data
            maestranza = Maestranza (nombre = data["nombre"], apellido = data["apellido"], dni = data["dni"], sector = data["sector"])
            maestranza.save()
            chequeo = print ("Se ha registrado con exito el formulario. Muchas Gracias")
            return render (request, "app/maestranza.html")
    else:
        formMaes = formMaestranza()
        return render (request, "app/maestranza.html",{"formMaes":formMaes})

def mostrar_Profesores(request):

    profesores = Profesor.objects.all()
    return render (request,  "app/mostrarProfesores.html", {"profesores": profesores})


def mostrar_Estudiantes(request):

    estudiantes = Estudiante.objects.all()
    return render (request,  "app/mostrarEstudiantes.html", {"estudiantes": estudiantes})


def mostrar_Maestranza(request):

    maestranza = Maestranza.objects.all()
    return render (request,  "app/mostrarMaestranza.html", {"maestranza": maestranza})

def buscar_estudiante(request):

    busquedaEstudiantes = form_busqueda_estudiantes()

    if request.GET:
        
        estudiantes = Estudiante.objects.filter(nombre=busquedaEstudiantes["criterio"]).all()
        
        return render (request, "app/busquedaEstudiantes.html", {"busquedaEstudiantes" : busquedaEstudiantes, "estudiantes" : estudiantes})
    
    return render (request, "app/busquedaEstudiantes.html", {"busquedaEstudiantes" :busquedaEstudiantes})