from pathlib import Path
from io import open

# ! Alternativa 1
# # ? leer archivos
# archivo = Path('archivos/prueba.txt')
# texto = archivo.read_text().split("\n") # split se puede usar para cada string y dice por que elemento se quiere dividir el string
# #print(texto)
# # ? modificar archivos
# texto.insert(0, "hola mundo")
# archivo.write_text("\n".join(texto), "utf-8") # escribe en el texto pero uniendo nuevamente el texto donde tenga espacio(\n)

# ! Alternativa 2
# # ? escribir archivos
# texto = "Hola mundo"
# archivo = open("archivos/hola-mundo.txt", "w") # "w" -> modo escritura
# archivo.write(texto)
# archivo.close()
# # ? leer archivos
# archivo = open("archivos/prueba.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)
# # ? lectura como lista
# archivo = open("archivos/prueba.txt", "r")
# texto = archivo.readline() # lee todas las lineas y las deja como un listado
# archivo.close()
# print(texto)
# ! Alternativa 3
# # ? lerr archivos
# with open("archivos/hola-mundo.txt", "r") as archivo:
#     # with abre y cierra el archivo automaticamente
#     #print(archivo.readlines())
#     for linea in archivo:
#         print(linea)
# # ? agregar archivos
# archivo = open("archivos/hola-mundo.txt", "a+")
# archivo.write(' Chao mundo')  
# archivo.close() 
# ? lectura y escritura
# with open("archivos/hola-mundo.txt", "r+") as archivo:
#     texto = archivo.readlines()
#     archivo.seek(0)
#     texto[0] = 'Chanchito feliz'
#     archivo.writelines(texto)