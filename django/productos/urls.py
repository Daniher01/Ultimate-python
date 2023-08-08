from django.urls import path
from . import views

#! convencio para poder llamar mas comodamente a la url de la app de producto
# luego en el template se llamaria, ejemplo, productos:detalle
app_name = 'productos'

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario', views.formulario, name='formulario'),
    path('<int:producto_id>', views.detalle,
         name='detalle'),  # productos:detalle
]
