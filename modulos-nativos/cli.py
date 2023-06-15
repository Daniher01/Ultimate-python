import os
from pathlib import Path
import sys

#print(sys.argv)
""" 
primer argumento: archivo que se ejecuta
segundo argumento en adelante: comados que se reciben por cli
"""

def cli(args):
    if len(args) == 1:
        print("No se pasaron argumentos")
        return
    if len(args) != 3:
        print('Se necesitan 2 argumentos')
        return
    
    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print('Origen no existe')
        return
    
    destino = args[2]
    d = Path(destino)
    if d.exists():
        print('Ya existe ese destino')
        return
    
    os.rename(str(origen), str(destino))
    print("Archivo renombrado con exito")

cli(sys.argv)