from bs4 import BeautifulSoup
import requests

url = "https://stackoverflow.com/questions"
respuesta = requests.get(url)
texto = respuesta.text
soup = BeautifulSoup(texto,"html.parser") #parsea el string que recibe a HTML

# permite obtener los elementos del html con el .select()
preguntas = soup.select(".s-post-summary")

for pregunta in preguntas:
    titulo = pregunta.select_one(".s-link").get_text()
    usuario = pregunta.select_one(".s-user-card--link").get_text()
    print(f"{usuario.strip()} - \nTitulo: {titulo.strip()}")