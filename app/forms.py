from django import forms

class formProfesores(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    asignatura = forms.CharField(max_length=40)

class formEstudiantes(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    curso = forms.IntegerField()

class formMaestranza(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    sector = forms.IntegerField()

class form_busqueda_estudiantes(forms.Form):
    criterio = forms.CharField()