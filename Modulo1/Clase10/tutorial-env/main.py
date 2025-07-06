import requests

url = "https://api.chucknorris.io/jokes/random"

respuesta = requests.get(url)

print("Frase", respuesta.json()["value"])  # Imprime la frase aleatoria de Chuck Norris
