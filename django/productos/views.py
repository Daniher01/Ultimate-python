from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
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
    return HttpResponse(producto_id)
