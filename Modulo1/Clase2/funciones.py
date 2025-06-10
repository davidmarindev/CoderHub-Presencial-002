# Funcines en programación:

# Una función es un bloque de código que realiza una tarea específica.
# Las funciones pueden recibir parámetros y devolver valores.

# Funciones propias de Python

# print
# type(nota_final)  # Imprime el tipo de dato de la variable nota_final
# input("Presione Enter para continuar...")
# int(nota_final)  # Convierte la nota final a entero
# float(nota_final)  # Convierte la nota final a float
# str(nota_final)  # Convierte la nota final a string

# Funciones definidas por el usuario

# Pasos para crear una función:
# 1. Definir la función con la palabra clave reservada def.
# 2. Escribir el nombre de la función.
# 3. Escribir los parámetros entre paréntesis.(Parametros: Son variables que recibe la función).
# 4. Escribir dos puntos al final de la línea, para indicar el inicio del bloque.
# 5. Escribir el cuerpo de la función con sangría(Bloque de codigo).
# 6. Llamar la función para ejecutarla.

def suma(a, b):
  """
  Esta función recibe dos números y devuelve su suma.
  :param a: Primer número
  :param b: Segundo número
  :return: Suma de a y b
  """
  return a + b

def resta(a, b):
  """
  Esta función recibe dos números y devuelve su resta.
  :param a: Primer número
  :param b: Segundo número
  :return: Resta de a y b
  """
  return a - b

def multiplicacion(a, b):
  """
  Esta función recibe dos números y devuelve su multiplicación.
  :param a: Primer número
  :param b: Segundo número
  :return: Multiplicación de a y b
  """
  return a * b

def division(a, b):
  """
  Esta función recibe dos números y devuelve su división.
  :param a: Primer número
  :param b: Segundo número
  :return: División de a y b
  """
  if b == 0:
    raise ValueError("No se puede dividir por cero")
  return a / b

valor_1 = int(input("Ingrese el primer número: "))
valor_2 = int(input("Ingrese el segundo número: "))

# print("Suma:", suma(valor_2, valor_1))
# print("División:", division(valor_2, valor_1))

opt = input("Elige una operación por el numero (1. suma, 2. resta, 3. multiplicación, 4. división): ")

if opt == "1":
    print("Resultado de la suma:", suma(valor_1, valor_2))
elif opt == "2":
    print("Resultado de la resta:", resta(valor_1, valor_2))
elif opt == "3":
    print("Resultado de la multiplicación:", multiplicacion(valor_1, valor_2))
elif opt == "4":
    try:
        print("Resultado de la división:", division(valor_1, valor_2))
    except ValueError as e:
        print("Hay un error", e)
else:
    print("Operación no válida. Por favor, elige una opción entre 1 y 4.")

# def imprimer_tres_lineas():

#   print()
#   print()
#   print()

# print("Hola a")
# imprimer_tres_lineas()
# print("Hola b")
# imprimer_tres_lineas()
# print("Chao")
# imprimer_tres_lineas()
# print("Chao a")

# def prueba_void():
#   """
#   Esta función no recibe parámetros ni devuelve valores.
#   Simplemente imprime un mensaje.
#   """
#   print("Esta es una función void, no retorna nada.")
    
# resultado_void = prueba_void()  # Llamada a la función void
# print("El resultado de la función void es:", resultado_void)  # Imprime None, ya que la función no retorna nada

# def prueba_retorno():
#   """
#   Esta función retorna un valor.
#   :return: Un mensaje de prueba
#   """
#   return "Esta es una función que retorna un valor."

# resultado_retorno = prueba_retorno()  # Llamada a la función que retorna un valor
# print("El resultado de la función que retorna un valor es:", resultado_retorno)  # Imprime el mensaje retornado

# def saludar(nombre):
#     """
#     Esta función recibe un nombre y devuelve un saludo.
#     :param nombre: Nombre de la persona a saludar
#     :return: Saludo personalizado
#     """
#     print("Hola", nombre)
    
# # "Hola" + " " + "Ricardo"  # Concatenación de strings
  
# def nombre_completo(nombre, apellido):
#     """
#     Esta función recibe un nombre y un apellido, y devuelve el nombre completo.
#     :param nombre: Nombre de la persona
#     :param apellido: Apellido de la persona
#     :return: Nombre completo
#     """
#     return nombre + " " + apellido
  
# name = input("Ingrese su nombre: ")
# last_name = input("Ingrese su apellido: ")

# full_name = nombre_completo(name, last_name) 

# saludar(full_name)