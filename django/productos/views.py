from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from .forms import ProductoForm
from .models import Producto

# Create your views here.

# /productos

# * return con objetos json


# def index(request):
#     productos = Producto.objects.all().values()
#     return JsonResponse(list(productos), safe=False)

# * return con plantillas html
def index(request):
    productos = Producto.objects.all()
    return render(
        request,
        'index.html',
        context={'productos': productos})


def detalle(request, producto_id):
    # ! alternativa a la linea de abajo, si no existe el valor, devuelve un objeto not found 404
    producto = get_object_or_404(Producto, id=producto_id)
    # producto = Producto.objects.get(id=producto_id)
    return render(
        request,
        'detalle.html',
        context={'producto': producto})


def formulario(request):
    # ? validar el formulario
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = ProductoForm()

    return render(
        request,
        'producto_form.html',
        context={'form': form}
    )
