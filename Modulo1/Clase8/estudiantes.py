# import sys

# if len(sys.argv) < 2:
#     print("Por favor, proporciona al menos un argumento.")
#     sys.exit(1)

# url_archivo = sys.argv[1]

estudiantes = [
      {"nombre": "Juan", "edad": 20, "carrera": "Ingeniería"},
      {"nombre": "Ana", "edad": 22, "carrera": "Medicina"},
      {"nombre": "Luis", "edad": 21, "carrera": "Arquitectura"},
      {"nombre": "María", "edad": 23, "carrera": "Derecho"}
    ]

# archivo = open('Estudiantes/archivo_estudiantes.txt', 'w')

# for estudiante in estudiantes:
#     archivo.write(f"{estudiante['nombre']}, {estudiante['edad']}, {estudiante['carrera']}\n")

# archivo.close()  # Cierra el archivo 

# archivo = open('Estudiantes/archivo_estudiantes.txt', 'a')

# nombre = input("Ingrese el nombre del estudiante: ")
# edad = input("Ingrese la edad del estudiante: ")
# carrera = input("Ingrese la carrera del estudiante: ")

# archivo.write(f"{nombre}, {edad}, {carrera}\n")

# archivo.close()  # Cierra el archivo

# Leer el archivo y mostrar su contenido

# archivo = open('Estudiantes/archivo_estudiantes.txt', 'r')  # Abre el archivo en modo lectura

# archivo_contenido = archivo.readlines()  # Lee todo el contenido del archivo

# for linea in archivo_contenido:
#   name, age, career = linea.split(', ')  # Divide cada línea en nombre, edad y carrera
#   print("Nombre", name)  # Imprime cada línea del archivo, separando por comas
#   print("Edad", age)
#   print("Carrera", career.strip())  # Elimina el salto de línea al final
  
# archivo.close()  # Cierra el archivo

# Elimar un estudiante del archivo

archivo = open('Estudiantes/archivo_estudiantes.txt', 'r+')  # Abre el archivo en modo lectura y escritura

archivo_contenido = archivo.readlines()  # Lee todo el contenido del archivo

nombre_a_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")

archivo.seek(0)  # Mueve el cursor al inicio del archivo
archivo.truncate()  # Elimina el contenido del archivo
for linea in archivo_contenido:
    name, age, career = linea.split(', ')  # Divide cada línea en nombre, edad y carrera
    if name.lower() != nombre_a_eliminar.lower():  # Si el nombre no es el que se quiere eliminar
        archivo.write(f"{name}, {age}, {career}")  # Escribe la línea en el archivo
        
archivo.close()  # Cierra el archivo