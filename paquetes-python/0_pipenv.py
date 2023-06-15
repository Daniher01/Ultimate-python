"""  
Una buena manera de gestionar paquetes con pipenv

pip install pipenv
-activarlo
    #? pipenv shell
- para que otro desarrollador use nuestras dependencias del proyecyo
    #? pipenv install --ignore-pipfile
"""


import requests

r = requests.get('https://www.google.com')
print(r)