from django.shortcuts import render, redirect
from .models import Autor, Libro, Editorial
from .forms import AutorForm, LibroForm, EditorialForm, BuscarForm

def agregar_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutorForm()
    return render(request, 'mi_aplicacion/formulario.html', {'form': form})

def agregar_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'mi_aplicacion/formulario.html', {'form': form})
    
def agregar_editorial(request):
    if request.method == "POST":
        form = EditorialForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('listar_editoriales')
    else:
        form = EditorialForm()
    return render(request, 'mi_aplicacion/formulario.html', {'form': form})

def buscar(request):
    form = BuscarForm
    resultados = []
    if 'query' in request.GET:
        query = request.GET['query']
        resultados = Libro.objects.filter(titulo_icontains=query)
    return render(request, 'mi_aplicacion/buscar.html', {'form': form, 'resultados': resultados})
