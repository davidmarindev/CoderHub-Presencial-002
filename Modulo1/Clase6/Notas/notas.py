# [10, 20, 30, 40, 50]
def calcular_nota_final(lista_notas):
  return sum(lista_notas) / len(lista_notas)

def nota_aprobatoria(nota):
  if nota >= 10:
    print("Aprobado")
  else:
    print("Reprobado")