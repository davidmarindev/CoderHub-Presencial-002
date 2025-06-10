# Ejercicio de crear una función que reciba una palabra y me devuelva cuantas vocales tiene mi palabra.

# Crear una función que reciba una palabra como argumento
# Necesito validar que es una vocal 
# Necesito un contador de vocales
# Necesito comparar letra por letra mi palabra para encontrar las vocales
# Cada vez que encuentre una vocal incremento mi contador

def es_vocal(letra):
	if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
		return True
	else:
		return False

def contador_vocales(palabra):
	contador = 0
	for letra in palabra:
		if es_vocal(letra.lower()):
			contador += 1
	
	print(f"La palabra {palabra} tiene {contador} vocales")
 

palabra = input("Ingrese una palabra: ")
contador_vocales(palabra)