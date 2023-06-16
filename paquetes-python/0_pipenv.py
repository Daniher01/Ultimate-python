"""  
Una buena manera de gestionar paquetes con pipenv

pip install pipenv
-activarlo
    #? pipenv shell
- instalar una dependencia
    #? pipenv install nombre_libreria    
- para que otro desarrollador use nuestras dependencias del proyecyo
    #? pipenv install --ignore-pipfile
- para ver las dependencias instalas en el proyecto
    #? pipenv graph    
- actualizar paquetes
    #? pipenv update    
"""


import requests

r = requests.get('https://www.google.com')
print(r)