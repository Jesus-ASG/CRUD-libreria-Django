from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro #importar modelo del libro
from .forms import LibroForm

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all() # recoge todos los datos de los libros
    return render(request, 'libros/index.html', {'libros': libros}) # manda los datos al archivo index.html

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None) # recoge todos los datos del formulario
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario}) # manda los datos a crear.html

def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')