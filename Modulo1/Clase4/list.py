# Estructuras de datos

# Datos compuestos en python

# Listas
# Diccionarios
# Tuplas

# Listas/Arreglos

# Las listas pueden acceder de manera dinamica a los datos almacenados con el indice
# Las listas son mutables

# Operaciones Basicas dentro de una listas

# Agregar
# Acceder
# Modificar
# Eliminar
# Buscar
# Iterar



# | | - | | - | | - | |

lista_simple = ["Mango", "Naranja", "Fresa"]
numeros = [1, 3, 4, 7, 88]

print(lista_simple[1])
print(numeros[3])

numeros[3] = 15

print(numeros[3])

#Listas anidadas
usuarios = [[1, "jose", "morales", 25], [2, "Ricardo", "Rodriguez", 26, [12, 13, 5]]]

print(usuarios[1][4])

# Agregar datos

lista_simple.append("Manzana")
lista_simple.insert(1, "Piña")  # Inserta "Piña" en la posición 1

print(lista_simple)

# Acceder 

print(lista_simple[0]) # Accede al primer elemento de la lista
print(lista_simple[-1]) # Accede a la ultima posicion de la lista

print(lista_simple[:2])
print(lista_simple[1:])
print(lista_simple[1:3])

# Modificar

lista_simple[2] = "Limon"

print(lista_simple)

lista_simple.sort() # Orderna la lista de manera ascendente

print(lista_simple)

lista_simple.reverse() # Revierte el orden de la lista

print(lista_simple)

# Eliminar

print("Antes de eliminar", lista_simple)
lista_simple.pop()  # Elimina el último elemento de la lista
lista_simple.pop(0)  # Elimina el primer elemento de la lista)
# lista_simple.clear()  # Elimina todos los elementos de la lista
lista_simple.remove("Mango")  # Elimina el primer elemento que coincida con el valor
print("Despues de eliminar", lista_simple)

# Buscar

print(lista_simple.index("Manzana"))

# Tamaño de la lista
print(len(lista_simple))  # Imprime el número de elementos en la lista

# Iterar sobre una lista

for fruta in lista_simple:
    print(f"Fruta: {fruta}")
    
index = 0
while index < len(lista_simple):
    print(f"Fruta en el índice {index}: {lista_simple[index]}")
    index += 1
    
    # print("Fruta en el índice", index, ":", lista_simple[index])  # Imprime la fruta en el índice actual