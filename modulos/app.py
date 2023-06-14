""" 
modulos -> archivos
paquetes -> carpetas
"""

from usuarios.impuestos.utilidades import pagar_impuestos
import usuarios

#pagar_impuestos()

# ? funcion dir
# print(dir(usuarios))
# print(usuarios.gestion.__name__)
# print(usuarios.impuestos.__package__)
# print(usuarios.gestion.__path__)
# print(usuarios.impuestos.__file__)

# ? paquetes dinamicos
print(__name__)