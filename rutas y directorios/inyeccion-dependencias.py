""" 
Hay dos maneras de hacer inyeccion de dependencias (en una clase)
1. pasando los parametros a través del constructor
2. creando una funcion "inicializadora" que pase esos parametros
"""

# ejemplo de inyeccion de dependencias
def init_app(bbdd, api):
    """ 
    indistintamente de cual sea la bbdd o la api que se le pase, si tiene los mismo metodo, la lógica será la misma,
    esto se puede logra con una interfaz para la bbdd o la api, asegurando que todas las bbdd heredadas de esa interfaz tengan los mismos metodos
    """
    pass