from django.shortcuts import redirect, render
# from django.views.generic.edit import DeleteView
from .forms import *
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import *
# from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
# def home(request):
#     return render(request,'index.html')
class Inicio(TemplateView):
    template_name = 'index.html'

class CrearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')

# def crearAutor(request):
#     if request.method == 'POST':
#         autor_form = AutorForm(request.POST)
#         if autor_form.is_valid():
#             autor_form.save()
#             return redirect('index')
#     else:
#         autor_form = AutorForm()
#     return render(request,'libro/crear_autor.html',{'autor_form':autor_form})



class ListadoAutor(ListView):
    model = Autor
    template_name = 'libro/autor/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado=True)
    
    # def get(self, request, *args,**kwargs):
    #     autores = Autor.objects.filter(estado=True)

    #     return render(request,self.template_name,{'autores':autores})


# def listarAutor(request):
#     autores = Autor.objects.filter(estado=True)
#     return render(request,'libro/autor/listar_autor.html',{'autores':autores})


class ActualizarAutor(UpdateView):
    model = Autor    
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')

# def editarAutor(request,id):
#     autor_form = None
#     error = None
#     try:        
#         autor = Autor.objects.get(id=id)
#         if request.method == 'GET':
#             autor_form = AutorForm(instance= autor)
#         else:
#             autor_form = AutorForm(request.POST, instance=autor)
#             if autor_form.is_valid():
#                 autor_form.save()
#             return redirect('index')
#     except Exception as e:
#         error = e 
#     return render(request,'libro/autor/crear_autor.html',{'autor_form':autor_form,'error':error})
    

class EliminarAutor(DeleteView):
    model = Autor

    def post(self, request, pk,*args, **kwargs):
        object = Autor.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('libro:listar_autor')

# def eliminarAutor(request,id):
#     autor = Autor.objects.get(id=id)
#     autor.estado = False
#     autor.save()
#     return redirect('libro:listar_autor')


    # if request.method == 'POST':
    #     autor.delete()
    #     return redirect('libro:listar_autor')
    # return render(request,'libro/eliminar_autor.html',{'autor':autor})


class ListadoLibros(ListView):
    model = Libro
    template_name = 'libro/libro/listar_libro.html'
    context_object_name = 'libros'
    queryset = Autor.objects.filter(estado=True)