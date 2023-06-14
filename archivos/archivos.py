from pathlib import Path
from time import ctime

archivo = Path("archivos/prueba.txt")
print(f'acesso: ', ctime(archivo.stat().st_atime))
print(f'creacion: ', ctime(archivo.stat().st_ctime))
print(f'modificacion: ', ctime(archivo.stat().st_mtime))