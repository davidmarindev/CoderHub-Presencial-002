def leer_archivo(nombre):
  archivo = open(nombre, 'r')  # Abre el archivo en modo lectura
  contenido = archivo.readlines()  # Lee todo el contenido del archivo
  
  for linea in contenido:
    print(linea.strip())  # Imprime cada línea del archivo, eliminando los saltos de línea
    
  archivo.close()  # Cierra el archivo
  print()

def escribir_archivo(nombre, contenido):
  pass

while True:
  print("1. Leer archivo")
  print("2. Escribir archivo")
  print("3. Salir")
  
  opcion = input("Seleccione una opción: ")
  
  if opcion == "1":
    nombre_archivo = input("Ingrese el nombre del archivo a leer: ")
    leer_archivo(nombre_archivo)
  elif opcion == "2":
    nombre_archivo = input("Ingrese el nombre del archivo a escribir: ")
    contenido = input("Ingrese el contenido a escribir: ")
    escribir_archivo(nombre_archivo, contenido)
  elif opcion == "3":
    print("Saliendo del programa.")
    break
  else:
    print("Opción no válida, intente de nuevo.")