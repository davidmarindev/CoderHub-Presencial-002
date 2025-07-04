usuarios = [
  {"username": "admin", "password": "admin123"},
  {"username": "user1", "password": "password1"},
  {"username": "user2", "password": "password2"},
  {"username": "user3"}
]

archivo = open("usuarios.txt", "w")
try:
    for usuario in usuarios:
        archivo.write(f"{usuario['username']}:{usuario['password']}\n")
except ZeroDivisionError as e:
    print(f"Error al escribir en el archivo: {e}")
finally:
    archivo.close()
    print("Archivo cerrado correctamente.")
