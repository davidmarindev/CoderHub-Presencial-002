# Diccionarios en Python
# Un diccionario es una colección de pares clave-valor.
# Se define utilizando llaves {} y cada par clave-valor se separa por dos puntos (:).
# Las claves deben ser únicas y pueden ser de cualquier tipo inmutable (como cadenas, números o tuplas).

usuario = {
    "nombre": "Juan",
    "edad": 30,
    "email": "juan@test.com",
    "direccion": {
        "calle": "Calle Falsa",
        "numero": 123,
        "ciudad": "Ciudad Ejemplo"
    },
    "telefonos": [123456789, 987654321],
}

# Acceso a los valores del diccionario
print(usuario["edad"])
print(usuario["direccion"]["ciudad"])
print(usuario["telefonos"][1])

# Modificación de un valor en el diccionario
usuario["edad"] = 31
print(usuario["edad"])

# Agregar un nuevo par clave-valor
usuario["ocupacion"] = "Ingeniero"
print(usuario)

# Eliminar un par clave-valor
del usuario["email"]
del usuario["direccion"]["numero"]  # Elimina el número de la dirección
print(usuario)

# Modificar nombre de una clave
usuario["nombre_completo"] = usuario.pop("nombre")  # Cambia la clave 'nombre' a 'nombre_completo'

# Keys y values metodos
print("Keys", usuario.keys()) # Imprime las claves del diccionario
print()
print("Values", usuario.values())  # Imprime los valores del diccionario

personas = [
    {
        "nombre": "Jose",
        "edad": 25,
        "email": "prueba@gmail.com"
    }, 
    {
        "nombre": "Jose",
        "edad": 25,
        "email": "prueba@gmail.com"
    },
    {
        "nombre": "Pablo",
        "edad": 25,
        "email": "prueba@gmail.com"
    }
]

print("Comparacion", personas[0] == personas[1]) # Compara si dos diccionarios son iguales

nueva_persona = { "nombre": "Maria", "edad": 25, "email": "prueba@gmail.com" }

personas.append(nueva_persona)  # Agrega una nueva persona al final de la lista

print("Cantidad de personas:", len(personas))  # Imprime la cantidad de personas en la lista

for persona in personas:
    print("Nombre:", persona["nombre"])
    
carro = {
    "brand": "Toyota",
    "modelo": "Corolla",
    "año": 2020,
    "color": "Rojo"
}

