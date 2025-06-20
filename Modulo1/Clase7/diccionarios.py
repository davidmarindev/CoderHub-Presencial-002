compras = {
  "Refresco": 1.50,
  "Pan": 0.80,
  "Leche": 1.20,
  "Carne": 5.00,
  "Frutas": 2.50,
  "Verduras": 1.80,
  "Cereal": 3.00,
  "Huevos": 2.00,
  "Arroz": 1.00,
}

print(compras.keys())  # Imprime las claves del diccionario
print(compras.values())  # Imprime los valores del diccionario
print(compras.items())  # Imprime las claves y valores del diccionario

print(sum(compras.values())) # Suma todos los valores del diccionario

for producto, precio in compras.items():
  print(f"Producto: {producto}, Precio: ${precio:.2f}")  # Imprime cada producto y su precio formateado a 2 decimales
  
for key in compras.keys():
  print(f"{key}: {compras[key]}")  # Imprime cada producto
  
personas = [
  {"nombre": "Juan", "edad": 30, "ciudad": "Madrid", "ci": "12345678"},
  {"nombre": "Ana", "edad": 25, "ciudad": "Barcelona", "ci": "87654321"},
  {"nombre": "Luis", "edad": 35, "ciudad": "Valencia", "ci": "11223344"},
  {"nombre": "María", "edad": 28, "ciudad": "Sevilla", "ci": "44332211"},
]

def buscar_persona_por_ci(ci):
    """Busca una persona por su CI en la lista de personas."""
    for persona in personas:
        if persona["ci"] == ci:
            return persona
    return "Persona no encontrada."
  
ci_buscar = input("Ingrese el CI de la persona a buscar: ")
persona_encontrada = buscar_persona_por_ci(ci_buscar)

print("Resultado de la búsqueda:", persona_encontrada)  # Imprime el resultado de la búsqueda

persona = {
  "nombre": "Carlos",
  "edad": 40,
  "ciudad": "Bilbao",
  "ci": "99887766"
}

print(type(persona))  # Imprime el tipo de dato del objeto persona

string = "Hola, soy un string"
print(isinstance(string, dict))  # Verifica si persona es un diccionario