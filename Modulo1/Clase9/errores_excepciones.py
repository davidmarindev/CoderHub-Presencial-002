# Errores y Excepciones en Python

# Errores: son problemas que ocurren durante la ejecución del programa y pueden ser causados por errores de sintaxis, errores lógicos, etc.
# Excepciones: son eventos que ocurren durante la ejecución del programa que interrumpen el flujo normal del programa. Las excepciones son un tipo de error que se puede manejar en Python

"""

Tipos de errores comunes en Python:

Estos errores suelen impedir que el código se ejecute:

SyntaxError: Error de sintaxis

IndentationError: Mala indentación

NameError: Se usa una variable que no existe

TypeError: Operación entre tipos incompatibles

ValueError: Tipo correcto pero valor inadecuado

ZeroDivisionError: División entre cero

IndexError: Índice fuera de rango en una lista

KeyError: Clave inexistente en un diccionario

FileNotFoundError: Archivo no encontrado

ImportError: Fallo al importar un módulo

AttributeError: Acceso a atributo que no existe

"""

"""
Principales excepciones que puedes manejar
Estas son clases que heredan de Exception, y por tanto puedes capturarlas con try/except:

ValueError

TypeError

ZeroDivisionError

FileNotFoundError

PermissionError

IndexError

KeyError

OSError

StopIteration

EOFError

AssertionError

"""

# Uso del raise para lanzar excepciones personalizadas 

print("Pasa por este punto del código")

# def dividir(a, b):
#     return a / b
  
# dividir(10, 0)  # Esto funciona correctamente

# try/except para manejar excepciones

def dividir_con_excepcion(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Error: No se puede dividir por cero. Detalles: {e}")
        return None
      
print("División de 10 entre 2:", dividir_con_excepcion(10, 0))

print("Llego a este punto del código")

# ValueError

def convertir_a_entero(valor):
    try:
        return int(valor)
    except ValueError as e:
        print(f"Error: No se puede convertir '{valor}' a entero. Detalles: {e}")
        return None
      
print("Conversión de 'abc' a entero:", convertir_a_entero('abc'))
print("Conversión de 'abc' a entero:", convertir_a_entero('22'))
print("Conversión de 'abc' a entero:", convertir_a_entero(True))
print("Conversión de 'abc' a entero:", convertir_a_entero("A"))

arr = [1, 2, 3, 4, 5, 6, 7]
# arr[4] == 5
# arr[10]  # Esto generará un IndexError


frutas = ["manzana", "banana", "naranja"]

try:
  input_fruta = input("Ingrese el nombre de una fruta para buscar el indice: ")

  index = frutas.index(input_fruta.lower())
  print(f"El índice de '{input_fruta}' es: {index} y el valor es: {frutas[index]}")
except IndexError as error:
  print(f"Error: El índice está fuera de rango. Detalles: {error}")
except ValueError as error:
  print(f"Error: La fruta '{input_fruta}' no se encuentra en la lista. Detalles: {error}")
  
# diccionario = {"a": 1, "b": 2, "c": 3}

# KeyError

personas = [
  { "nombre": "Juan", "edad": 30, "ciudad": "Madrid" },
  { "nombre": "Ana", "edad": 25, "ciudad": "Barcelona" },
  { "nombre": "Luis", "edad": 35, "ciudad": "Valencia" }
]

for persona in personas:
  try:
    print("Nombre", persona["nombre"])
    print("Ciudad", persona["ciudad"])
    # Intentamos acceder a una clave que no existe
    print("Edad", persona.get('age', 'no tiene edad'))  # Esto generará un KeyError
  except KeyError as error:
    print(f"Error: La clave {error} no existe en el diccionario")
    
# Uso del raise para lanzar excepciones personalizadas

def validar_edad(edad):
    if edad < 0:
        raise ValueError(f"La edad no puede ser negativa ({edad})")
    elif edad > 120:
        raise ValueError(f"La edad no puede ser mayor a 120 - ({edad})")
    else:
        print(f"La edad {edad} es válida")

try:
    edad = int(input("Ingrese su edad: "))
    validar_edad(edad)
except ValueError as ve:
    print(f"Error al validar la edad: {ve}")
except Exception as e:
    print(f"Error al validar la edad: {e}")

print("Fin del programa")

# Ejemplo de uso de f-strings para formatear cadenas
# age = 10
# f"La edad es {age}" -> "La edad es 10"

# nombre = "Juan"
# apellido = "Pérez"
# f"Hola, mi nombre es {nombre} {apellido}" -> "Hola, mi nombre es Juan Pérez"


