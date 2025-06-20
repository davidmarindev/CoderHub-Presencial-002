import requests

url = "https://jsonplaceholder.typicode.com/users"

respuesta = requests.get(url)

print("Código de estado:", respuesta.status_code)  # Imprime el código de estado de la respuesta

users = respuesta.json()  # Convierte la respuesta JSON a un objeto Python
print(users[0])

for user in users:
    print(f"Nombre: {user['name']}, Email: {user['email']}")  # Imprime el nombre y el email de cada usuario
    print(f"Dirección: {user['address']['street']}, {user['address']['city']}")  # Imprime la dirección de cada usuario
    print(f"Teléfono: {user['phone']}, Sitio web: {user['website']}")  # Imprime el teléfono y el sitio web de cada usuario
    print("-" * 40)  # Imprime una línea separadora