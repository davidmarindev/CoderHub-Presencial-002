# Variables Globales y Locales

# Una variable global es aquella que se define fuera de cualquier función 
# y puede ser accedida desde cualquier parte del código.

# Una variable local es aquella que se define dentro de una función o un ciclo,
# y solo puede ser accedida dentro de esa función o ciclo.

variable_global = "Soy una variable global"

def funcion_prueba():
    variable_local = "Soy una variable local"
    print(variable_global)  # Acceso a la variable global
    print(variable_local)   # Acceso a la variable local
    
funcion_prueba()
print(variable_global)
# print(variable_local) # Esto generaría un error, ya que variable_local no está definida fuera de la función

nombre = "Juan"

def cambiar_nombre():
    global nombre  # Declaramos que vamos a usar la variable global 'nombre'
    nombre = "Pedro"  # Cambiamos el valor de la variable global
    
cambiar_nombre()
print(nombre)  # Imprime "Pedro", ya que la variable global fue modificada

# Constantes

# En Python, no hay una forma nativa de definir constantes como en otros lenguajes.
# Sin embargo, por convención, se utilizan nombres en mayúsculas para indicar que una variable es una constante.
PI = 3.14159  # Esta es una constante, aunque en Python se puede cambiar su valor.