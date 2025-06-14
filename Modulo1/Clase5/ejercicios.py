colores = ["Red", "Green", "Blue", "Yellow", "Black"]

for color in colores:
    print(color)
    
colores.append("White")  # Agrega un nuevo color al final de la lista

print("Lista de colores actualizada:", colores)  # Imprime la lista de colores actualizada

def palabra_a_binario(p):
    palabra_binario = []
    for letra in p:
        palabra_binario.append(format(ord(letra), '08b'))
        
    return palabra_binario

palabras = ["Python", "Java", "Ruby", "JavaScript", "php", "C++", "C#", "Swift"]

palabras_binario = {}

for palabra in palabras:
    palabra_min = palabra.lower()  # Convierte la palabra a minúsculas
    palabras_binario[palabra_min] =  palabra_a_binario(palabra_min) 
    
print("Palabras en binario:", palabras_binario)  # Imprime el diccionario de palabras en binario


arreglo = [1,2,3,4,5,6,7,8,9,10]
print(arreglo[0])

nuevo_arreglo = []

for num in arreglo:
    nuevo_arreglo.append(num * 2)  # Multiplica cada número por 2 y lo agrega al nuevo arreglo
    
for i in range(len(arreglo)):
    arreglo[i] = arreglo[i] * 2