import requests

# ? obtener recurso GET
url = "https://jsonplaceholder.typicode.com/users"

r = requests.get(url # url de la consulta
                 , timeout=10 #si no response la peticion en ese tiempo se da por terminada
                 )
r = r.json()

for user in r:
    print(user['name'])
    
# ? crear recurso POST
url = "https://jsonplaceholder.typicode.com/users"
user = {
    "name": "Nombre editado DH"
}
r = requests.post(url, timeout=10, data=user)
print(r.status_code)

# ? PUT/PATCH
url = "https://jsonplaceholder.typicode.com/users/2"
user = {
    "name": "Nombre editado DH"
}
r = requests.put(url, timeout=10, data=user)
print(r.status_code)

# ? DELETE
url = "https://jsonplaceholder.typicode.com/users/2"

r = requests.delete(url, timeout=10)
print(r.status_code)