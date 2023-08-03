""" 
Para las apis que esten protegidas, hay que pasasrle el token en le header
"""

import requests

# token
apikey = "123456"
# headers
headers = {
    "Autorization": f"Bearer {apikey}"
}

# ? obtener recurso GET
url = "https://jsonplaceholder.typicode.com/users/1"

r = requests.get(url # url de la consulta
                 , timeout=10 #si no response la peticion en ese tiempo se da por terminada
                 , headers=headers # headers para pasarle la apikey
                 )
r = r.json()
print(r['name'])

# ? crear recurso POST
url = "https://jsonplaceholder.typicode.com/users"
user = {
    "name": "Nombre editado DH"
}
r = requests.post(url, timeout=10, data=user, headers=headers)
print(r.status_code)

# ? PUT/PATCH
url = "https://jsonplaceholder.typicode.com/users/2"
user = {
    "name": "Nombre editado DH"
}
r = requests.put(url, timeout=10, data=user, headers=headers)
print(r.status_code)

# ? DELETE
url = "https://jsonplaceholder.typicode.com/users/2"

r = requests.delete(url, timeout=10, headers=headers)
print(r.status_code)