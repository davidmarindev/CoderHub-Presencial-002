import math
import random
import os
import sys

# Ejemplo de uso del módulo math
def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    area = math.pi * (radio ** 2)
    return area
  
area_circulo = calcular_area_circulo(5)  # Calcula el área de un círculo con radio 5

# Truncar el area a 2 decimales
area_circulo = round(area_circulo, 2)

print("Área de un círculo con radio 5:", calcular_area_circulo(5))
print("Raíz cuadrada de 16:", math.sqrt(16))  # Ejemplo de uso de la función sqrt del módulo math
print("Valor de pi:", math.pi)  # Imprime el valor de pi del módulo math

print("Factorial de 5:", math.factorial(5))  # Imprime el factorial de 5

# Floor y Ceil
print("Redondeo hacia abajo de 3.7:", math.floor(3.7))  # Redondea hacia abajo
print("Redondeo hacia arriba de 3.7:", math.ceil(3.7))  # Redondea hacia arriba

numeros_rifa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ejemplo de uso del módulo random
def generar_numero_aleatorio(superior, inferior=0):
    print("Generando un número aleatorio entre", inferior, "y", superior)
    """Genera un número aleatorio entre inferior y superior."""
    return random.randint(inferior, superior)
  
numero_aleatorio = generar_numero_aleatorio(len(numeros_rifa) - 1, 2)

print("Numero ganador", numeros_rifa[numero_aleatorio])

random_float = random.uniform(1, 10)  # Genera un número aleatorio de punto flotante entre 1 y 10
print("Número aleatorio de punto flotante entre 1 y 10:", random_float)

lista_colores = ["Rojo", "Verde", "Azul", "Amarillo", "Negro"]

colores_aleatorios = random.sample(lista_colores, 2)  # Selecciona 2 colores aleatorios de la lista

print("Colores aleatorios seleccionados:", colores_aleatorios)

# Ejemplo de uso del módulo os
def listar_archivos_directorio(directorio):
    """Lista los archivos en un directorio dado."""
    try:
        archivos = os.listdir(directorio)
        return archivos
    except FileNotFoundError:
        return "El directorio no existe."

directorio_actual = os.getcwd()  # Obtiene el directorio de trabajo actual
print("Directorio actual:", directorio_actual)
print("Archivos en el directorio actual:", listar_archivos_directorio(directorio_actual))

path = "/Users/davidmaring7/Documents/CoderHub/CoderHubPractica/CursoPresencial002/Modulo1/Clase8"

print("Archivos en el directorio especificado:",  listar_archivos_directorio(path))

# Ejemplo de uso del módulo sys
def imprimir_version_python():
    """Imprime la versión de Python que se está utilizando."""
    print("Versión de Python:", sys.version)
imprimir_version_python()

def imprimir_ruta_python():
    """Imprime la ruta de búsqueda de módulos de Python."""
    print("Ruta de búsqueda de módulos:", sys.path)
imprimir_ruta_python()