from . import models
from django.forms import ModelForm

# ? formularios en base a modelos
""" 
son plantillas de formulario donde django ya nos da el esquema y las validaciones necesarias para ese modelo,
para esto ese necesario instalar la aplicacion de forms en settings.py
"""


class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = ['nombre', 'stock', 'puntaje', 'categoria']
