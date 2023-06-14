from pathlib import Path
from zipfile import ZipFile

# #? escribir 
# with ZipFile('archivos/comprimido.zip', 'w') as zip:
#     #path = carpeta actual donde se ejecuta (carpeta raiz del proyecto)
#     for path in Path().rglob("*.py"):
#         print(path)
#         if str(path) != "archivos/comprimidos.zip":
#             zip.write(path)

#? leer
with ZipFile('archivos/comprimido.zip') as zip:
    #print(zip.namelist())
    info = zip.getinfo("archivos/comprimidos.py") # inspeccionar un archivo especifico
    print(
        info.file_size,
        info.compress_size
    )
    zip.extractall("archivos/descomprimidos") # lo descomprime en una carpeta