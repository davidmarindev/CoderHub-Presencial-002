# Metodos de las listas

# Listas en Python

# in
# not in
# sort
# reverse
# sum
# mix
# max

numeros = [1 ,2 ,3 ,4]

print(7 not in numeros)
print("Hola" in "Hola Mundo")

# numeros.sort()  # Ordena la lista en orden ascendente

numeros_desordenados = [3, 1, 4, 2]

print("Lista original:", numeros_desordenados)
numeros_desordenados.sort()  # Ordena la lista en orden ascendente
print("Lista ordenada:", numeros_desordenados)

# numeros.reverse()  # Invierte el orden de los elementos en la lista
numeros_invertidos = [5, 4, 3, 2, 1]
print("Lista original:", numeros_invertidos)
numeros_invertidos.reverse()  # Invierte el orden de los elementos en la lista
print("Lista invertida:", numeros_invertidos)

print("Tipo de datos de la lista:", type(numeros))  # Imprime el tipo de datos de la lista

# count

print("Número de veces que aparece el 2 en la lista:", numeros.count(2))  # Cuenta cuántas veces aparece el número 2 en la lista

print("Suma de los números:", sum(numeros))  # Suma todos los elementos de la lista
print("Número máximo en la lista:", max(numeros))  # Encuentra el número máximo en la lista
print("Número mínimo en la lista:", min(numeros))  # Encuentra el número mínimo en la lista
print("Longitud de la lista:", len(numeros))  # Obtiene la longitud de la lista

votos = ["Karen", "Karen", "Karen", "Juan", "Juan", 
         "Pedro", "Pedro", "Pedro", "Moises", 
         "Moises", "Moises", "Moises", "Karen"]

hash_votos = {}

for voto in votos:
    if voto in hash_votos:
        hash_votos[voto] += 1  # Incrementa el contador si el voto ya existe
    else:
        hash_votos[voto] = 1  # Inicializa el contador si el voto no existe
        
print("Votos por candidato:", hash_votos)  # Imprime el diccionario de votos por candidato

print(set(votos))

lista_sin_duplicados = list(set(votos))
print("Lista de votos sin duplicados:", lista_sin_duplicados)  # Imprime la lista de votos sin duplicados

# Sets son colecciones de elementos únicos y no ordenados.
# Los sets no permiten duplicados y son útiles para eliminar elementos repetidos de una lista.

print(dict.fromkeys(votos, 0))  # Crea un diccionario con los votos como claves y 0 como valor inicial


var_string = 'Hola mundo desde Python'

print(var_string.split(" "))  # Divide la cadena en una lista de palabras

word_array = var_string.split(" ")

print(", ".join(word_array))  # Une las palabras de la lista en una sola cadena separada por espacios

numeros = [2, 5, 3, 99, 1, 54, 77, 23, 12, 45, 67, 89]

def min_max(lista):
    max = 0
    min = lista[0]

    for num in lista:
      if num > max:
          max = num
      if num < min:
          min = num
    return min, max
  
minimo, maximo = min_max(numeros)

print("Número mínimo:", minimo)  # Imprime el número mínimo
print("Número máximo:", maximo)  # Imprime el número máximo

def palimdromo(palabra):
    palabra = palabra.lower()  # Convierte la palabra a minúsculas
    # return palabra == palabra[::-1]  # Compara la palabra con su reverso

    nueva_lista = list(palabra)
    nueva_lista.reverse()  # Invierte la lista de caracteres
    palabra_reversa = "".join(nueva_lista)
    print("Palabra invertida:", palabra_reversa)  # Imprime la palabra invertida
    
    return palabra == palabra_reversa  # Compara la palabra con su reverso

# palabra = "radar"
# lista_palabra = list(palabra)
# lista_palabra.reverse() # Convierte la palabra en una lista de caracteres
# print(lista_palabra)  # Invierte la lista de caracteres
  
print("¿La palabra 'radar' es un palíndromo?", palimdromo("radar"))  # Verifica si "radar" es un palíndromo
print("¿La palabra 'Python' es un palíndromo?", palimdromo("Python"))  # Verifica si "Python" es un palíndromo

