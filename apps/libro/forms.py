from django import forms
from django.forms import widgets
from .models import *

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellidos','nacionalidad','descripcion']
        labels = {
            'nombre':'Nombre del autor',
            'apellidos':'Apellidos del autor',
            'nacionalidad':'Nacionalidad del autor',
            'descripcion':'Pequeña descripción'
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre del autor'}),
            'apellidos':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese apellidos del autor'}),
            'nacionalidad':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nacionalidad del autor'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control','placeholder':'Ingrese descripción del autor'})
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('titulo','autor_id','fecha_publicacion')
        label = {
            'titulo':'Título del libro',
            'autor_id':'Autor(es) del libro',
            'fecha_publicacion':'Fecha de Publicación del libro'
        }
        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese título de libro'}),
            'autor_id':forms.SelectMultiple(attrs={'class':'form-control'}),
            'fecha_publicacion':forms.SelectDateWidget(attrs={'class':'form-control'})
        }