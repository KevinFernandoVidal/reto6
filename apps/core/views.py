from django.shortcuts import redirect, render
from apps.core.models import Categoria, Sitio
from .forms import form_sito, from_categoria
import folium

# Create your views here.
def home(request):
    object = Categoria.objects.all()
    m = folium.Map(location=[12.5588533,-81.6980733],zoom_start=11.5)
    m = m._repr_html_()
    return render(request, 'core/home.html', locals())

def sitio_add(request):
    if request.method == 'POST':
        form_s = form_sito(request.POST, request.FILES)
        if form_s.is_valid():
            form_s.save()
            return redirect('/')
    else:
        form_s = form_sito()
    return render(request, 'core/sitio_add.html', locals())

def categoria_add(request):
    if request.method == 'POST':
        form_c = from_categoria(request.POST)
        if form_c.is_valid():
            form_c.save()
            return redirect('/')
    else:
        form_c = from_categoria()
    return render(request, 'core/categoria_add.html', locals())

def categoria_list(request, id_categoria):
    object = Sitio.objects.filter(categoria = id_categoria)
    return render(request, 'core/categoria_lista.html', locals())

def sitio(request, id_sitio):
    object = Sitio.objects.get(id = id_sitio)
    return render(request, 'core/sitio.html', locals())
