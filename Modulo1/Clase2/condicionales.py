# Condicionales: Son operadores que definen el flujo de mi aplicación

#if
#elif
#else

edad = 120

if(edad >= 18 and edad < 120):
  print("Es mayor de edad")
elif(edad < 0):
  print("Edad no válida")
elif(edad >= 120):
  print("Eres vampiro")
else:
  print("Es menor de edad")
  
