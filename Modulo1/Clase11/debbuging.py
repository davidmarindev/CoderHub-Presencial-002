# Debbuging en Python

# El debbuging es el proceso de encontrar y corregir errores en el código.
# Existen varias herramientas y técnicas para hacer debbuging en Python, algunas de las más comunes son:
# - print(): Imprimir el valor de las variables en diferentes puntos del código para ver qué está pasando.
# - pdb: El depurador de Python, que permite ejecutar el código paso a paso y ver el valor de las variables en cada paso.
# - breakpoints: Puntos de interrupción que permiten detener la ejecución del código en un punto específico y ver el valor de las variables en ese momento.

# Breakpoints en Visual Studio Code:
# - Puedes agregar un breakpoint haciendo clic en el margen izquierdo del editor de código, al lado del número de línea.
# - Cuando el código se ejecuta, se detendrá en el breakpoint y podrás ver el valor de las variables en ese momento.
# - Puedes usar la consola de depuración para ejecutar comandos y ver el valor de las variables.
# - Puedes continuar la ejecución del código paso a paso, saltar al siguiente breakpoint o salir del depurador. 

# Ejemplo de breakpoint en Visual Studio Code:
def suma(a, b):
    resultado = a + b
    return resultado
  
suma(5, 10)  # Aquí puedes agregar un breakpoint para ver el valor de 'resultado'

# Ejemplo pdb:
import pdb

def resta(a, b):
    pdb.set_trace()  # Aquí se detendrá la ejecución y podrás ver el valor de 'a' y 'b'
    resultado = a - b
    return resultado


def multiplicacion(a, b):
    breakpoint()  # Aquí se detendrá la ejecución y podrás ver el valor de 'a' y 'b'
    resultado = a * b
    return resultado

def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    option = input("Seleccione una opción: ")
    if option == "1":
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        print(f"La suma es: {suma(a, b)}")
    elif option == "2":
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        print(f"La resta es: {resta(a, b)}")
    elif option == "3":
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        print(f"La multiplicación es: {multiplicacion(a, b)}")
    else:
        print("Opción no válida")

menu()  # Aquí puedes ver el valor de 'resultado' en la consola de pdb

# funcion breakpoint() de pdb:

# multiplicacion(5, 10)  # Aquí puedes ver el valor de 'resultado' en la consola de pdb

# def saludo(nombre, apellido):
#     print(nombre)
#     print(apellido)
#     print(f"Hola mi nombre completo es:  {nombre} {apellido}")

# def mostrar_saludos(personas):
#     for persona in personas:
#         saludo(persona["nombre"], persona["apellido"])
        
# personas = [
#     {"nombre": "Juan", "apellido": "Pérez"},
#     {"nombre": "Ana", "apellido": ""},
#     {"nombre": "Luis" , "apellido": []},
# ]

# mostrar_saludos(personas)
