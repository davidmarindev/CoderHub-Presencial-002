# 0 1 2 3 4 5 6 7 8 9 10 - Base 10
# 0 1 2 3 4 10 12 13 14 20 - Base 5

# 0 1 10 11 100 101 110 111 - Base 2

# bit = 0 o 1 # bit es un dígito en el sistema binario

# Con 8 bits podemos representar 256 números diferentes, desde 0 hasta 255.

# 128 # 64 # 32 # 16 # 8 # 4 # 2 # 1

# 11111111 - 255

# 00000000 - 0

# 01000011 - 67

# 11000011 - 195

# 00010001 - 17

# 00100011 - 35

# 00000000 00100011 00100011 - Color

# Representar numeros a binario con python

print(ord('A')) # Imprime el valor ASCII de 'A'
print(ord('H'))
print(ord('/'))

print(format(ord('A'), '08b'))  # Imprime el valor ASCII de 'A' en binario con 8 bits
print(bin(65))  # Imprime el número 65 en binario

palabra = "Hola"

palabra_binario = []

for letra in palabra:
  print(format(ord(letra), '08b'))# Imprime el valor ASCII de cada letra en binario con 8 bits
  palabra_binario.append(format(ord(letra), '08b'))  # Agrega el valor binario de cada letra a la lista
  
print("Palabra en binario:", palabra_binario)  # Imprime la lista de valores binarios de cada letra

palabra_binario_str = ' '.join(palabra_binario)  # Une los valores binarios en una cadena separada por espacios
print("Palabra en binario como cadena:", palabra_binario_str)  # Imprime la cadena de valores binarios