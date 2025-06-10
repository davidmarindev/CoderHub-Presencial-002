# Ciclos, Bucles, Loops, Iteradores.

# Ciclo for: Es un ciclo que se utiliza para iterar sobre una secuencia 
# (como una lista, tupla, cadena de texto, etc.) o un rango de números.

def  imprimir_numeros():
    print("Imprimiendo números del 1 al 10:")
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")
    print("6")
    print("7")
    print("8")
    print("9")
    print("10")

imprimir_numeros()

for elemento in range(1, 101, 5):
    print(elemento)

for letra in "Python es un lenguaje de programación":
    if letra == " ":
        continue  # Salta los espacios en blanco
    print(letra)

palabra = "Python 3"
# |P|# |y| # |t|# |h|# |o|# |n|# | |# |3|
print(palabra[0])
print(palabra[6])
print(palabra[7])
    
arreglo = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

for elemento in arreglo:
    print(elemento)
    
letras = ["a", "b", "c", "d", "e"]

for letra in letras:
    print(letra)
    
# Ciclo while: Es un ciclo que se ejecuta mientras una condición sea verdadera.

num = 1
while num <= 10:
    print(num)
    num += 1 # Incrementa num en 1 en cada iteración
    
# Vuelta 1: num = 1 y 1 es menor o igual a 10, se imprime 1 y se incrementa num a 2
# Vuelta 2: num = 2 y 2 es menor o igual a 10, se imprime 2 y se incrementa num a 3
# Vuelta 3: num = 3 y 3 es menor o igual a 10, se imprime 3 y se incrementa num a 4
# Vuelta 4: num = 4 y 4 es menor o igual a 10, se imprime 4 y se incrementa num a 5
# Vuelta 5: num = 5 y 5 es menor o igual a 10, se imprime 5 y se incrementa num a 6
# Vuelta 6: num = 6 y 6 es menor o igual a 10, se imprime 6 y se incrementa num a 7
# Vuelta 7: num = 7 y 7 es menor o igual a 10, se imprime 7 y se incrementa num a 8
# Vuelta 8: num = 8 y 8 es menor o igual a 10, se imprime 8 y se incrementa num a 9
# Vuelta 9: num = 9 y 9 es menor o igual a 10, se imprime 9 y se incrementa num a 10
# Vuelta 10: num = 10 y 10 es menor o igual a 10, se imprime 10 y se incrementa num a 11
# Vuelta 11: num = 11 y 11 no es menor o igual a 10, se sale del ciclo
print("Fin del ciclo while")

while True:
    respuesta = input("¿Desea continuar? (s/n): ")
    print("Comparacion", "S" == "s")
    match respuesta.lower(): # lower() convierte string a minúsculas
        case "s":
            print("Continuando...")
            continue  # Vuelve al inicio del ciclo
        case "n":
            print("Saliendo del ciclo...")
            break  # Sale del ciclo
        case _:
            print("Respuesta no válida, por favor ingrese 's' o 'n'.")
            continue  # Vuelve al inicio del ciclo
        
# Inicia el ciclo while
# Respuesta del usuario
# Si la respuesta es "s", se imprime "Continuando..." y se vuelve al inicio del ciclo
# Si la respuesta es "n", se imprime "Saliendo del ciclo..." y se sale del ciclo
# Si la respuesta es diferente a "s" o "n", se imprime "Respuesta no válida, por favor ingrese 's' o 'n'." y se vuelve al inicio del ciclo

# count = 0
# while count < 5:
#     print("Contador:", count)
    
# ciclos anidados: Son ciclos dentro de otros ciclos.
for i in range(3):  # Ciclo externo
    print("Ciclo externo, iteración:", i)
    for j in range(5):  # Ciclo interno
        print("  Ciclo interno, iteración:", j)
