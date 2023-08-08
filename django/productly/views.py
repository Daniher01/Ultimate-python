"""
archivo de inicio del proyecto
independientemente de si tiene o no aplicaciones
"""
from django.shortcuts import render


def inicio(request):
    return render(
        request,
        'inicio.html'
    )
