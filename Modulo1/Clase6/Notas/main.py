import notas

n1 = float(input("Ingrese la primera nota: "))  # 10
n2 = float(input("Ingrese la segunda nota: "))  # 20
n3 = float(input("Ingrese la tercera nota: "))  # 30
n4 = float(input("Ingrese la cuarta nota: "))  # 40
n5 = float(input("Ingrese la quinta nota: "))  # 50
notas_usuario = [n1, n2, n3, n4, n5]

result = notas.calcular_nota_final(notas_usuario)

print("La nota final es:", result)  # Imprime la nota final calculada

notas.nota_aprobatoria(result)