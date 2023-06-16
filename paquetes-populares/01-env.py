# Variables de entorno
""" 
Guardar las variables de entorno en el arhcivo .env
# ? .env tiene que estar a la misma altura que el archivo pipfile
    ejemplo de archivo de .env:
        SENDGRID_API_KEY = "aslkneoifnadcnsdlvnldkcnñieflkas"
"""
import os

apikey = os.environ.get("SENDGRID_API_KEY")
print(apikey)