import csv
import os 

# #? escribir
# with open('archivos/archivo.csv', 'w') as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(['twit_id', "user_id", "text"]) 
#     writer.writerow([1000, 1, "este es un twit"]) 
#     writer.writerow([1001, 2, "otro twit"]) 
# #? leer
# with open('archivos/archivo.csv') as archivo:
#     reader = csv.reader(archivo)
#     for linea in reader:
#         print(linea)
#? actualizar
"""
no se puede leer y escribir un archivo al mismo tiempo
asi que en este caso, hay que crear un archivo temporal
donde se irá escribiendo los datos mientras que en el original se pueden ir leyendo
"""        
with open("archivos/archivo.csv") as r, open("archivos/archivo_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea:
            if linea[0] == "1000":
                writer.writerow([1000,1,'texto modificado'])
            else:
                writer.writerow(linea)
os.remove("archivos/archivo.csv") # elimina el archivo
os.rename("archivos/archivo_temp.csv", "archivos/archivo.csv")  # crea el archivo          