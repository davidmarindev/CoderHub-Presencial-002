# Una sentencia es una instrucción que puede ejecutar el 
# interprete de Python. Por ejemplo, una asignación es una sentencia.
# a = 5

# Expresiones
# Una expresión es una combinación de valores, variables y operadores.

name = "Ricardo"
last_name = "Rodriguez"
full_name = name + " " + last_name  # Concatenación de strings

# nota1 = 8.5
# nota2 = 9.0
# nota3 = 15

# nota_final = (nota1 + nota2 + nota3) // 3  # Cálculo del promedio

print("Nombre completo:", full_name)
# print("Nota final:", nota_final)

nota1 = input("Ingrese la primera nota: ")
nota2 = input("Ingrese la segunda nota: ")
nota3 = input("Ingrese la tercera nota: ")

"13" + "5"  # Esto es una expresión que concatena dos strings

print(type(nota1))  # Imprime el tipo de dato de la variable nota1

nota_final = (float(nota1) + float(nota2) + float(nota3)) / 3  # Cálculo del promedio

print("Nota final:", nota_final)