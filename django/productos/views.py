from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
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
