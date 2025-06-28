## Archivos en python

# Nos permite leer y escribir archivos, para persistir datos

## Abrir un archivo

# open('nombre_archivo', 'modo') -> 'r' -> read, 'w' -> write, 'a' -> append

## Modos de apertura de archivos

# 'r' -> read -> leer
# 'w' -> write -> escribir
# 'a' -> append -> agregar contenido

# 'r+' -> read and write -> leer y escribir
# 'w+' -> write and read -> escribir y leer

## Crear un archivo

# open('nombre_archivo', 'w')

## Leer un archivo

# read() -> lee todo el contenido del archivo

# readline() -> lee una linea del archivo

# readlines() -> lee todas las lineas del archivo

## Escribir en un archivo

# write('contenido')

# Cerrar un archivo

# close()

# Crear un archivo y escribir en él.

# archivo = open('archivo_prueba.txt', 'w')  # Abre el archivo en modo escritura (se crea si no existe)

# archivo.write('Hola, este es un archivo de prueba en python.\n')  # Escribe una línea en el archivo
# archivo.write('Esta es la segunda línea del archivo.\n')
# archivo.write('Y esta es la tercera línea del archivo.\n')

# archivo.close()  # Cierra el archivo

# Leer un archivo existente y mostrar su contenido

# archivo = open('archivo_prueba.txt', 'r')  # Abre el archivo en modo lectura

# archivo_contenido = archivo.readlines()  # Lee todo el contenido del archivo

# for linea in archivo_contenido:
#     print(f"Linea {archivo_contenido.index(linea)}", linea.strip())  # Imprime cada línea del archivo, eliminando los saltos de línea

# archivo.close()  # Cierra el archivo

# Agregar contenido a un archivo existente

# archivo = open('archivo_prueba.txt', 'a')  # Abre el archivo en modo append (agregar contenido)

# archivo.write('Esta es una nueva línea agregada al archivo.\n')  # Agrega una nueva línea al final del archivo

# archivo.close()  # Cierra el archivo


# Leer y escribir en un archivo al mismo tiempo

archivo = open('archivo_prueba.txt', 'r+')  # Abre el archivo en modo lectura y escritura

archivo.seek(1)
archivo.write('Esta es una nueva línea agregada al archivo 3.\n')  # Agrega una nueva línea al final del archivo

archivo.close()  # Cierra el archivo



