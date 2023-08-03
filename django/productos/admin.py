from django.contrib import admin
from .models import Categoria, Productos

# opcional


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Productos)
