# from calculadora import suma, resta
import calculadora

print("Esta es una calculadora simple en Python")

numero1 = float(input("Ingrese el primer número: ")) #3
numero2 = float(input("Ingrese el segundo número: "))  #4
operacion = input("Ingrese la operación a realizar (+, -, *, /): ") # +

def calcular(numero1, numero2, operacion):
  match operacion:
    case '+':
        return calculadora.suma(numero1, numero2) #7
    case '-':
        return numero1 - numero2
    case '*':
        return numero1 * numero2
    case '/':
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Error: División por cero no permitida."
    case _:
        return "Operación no válida."
      

resultado = calcular(numero1, numero2, operacion)

print(f"El resultado de {numero1} {operacion} {numero2} es: {resultado}")
