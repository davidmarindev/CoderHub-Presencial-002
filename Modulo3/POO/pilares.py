#Pilares de la POO
# - Abstracción
# - Encapsulamiento
# - Herencia
# - Polimorfismo

# Abstracción: 

""" La abstracción en POO es el principio de ocultar los detalles de implementación 
complejos y exponer solo las características esenciales de un objeto. Permite modelar 
sistemas complejos de forma simplificada al concentrarse 
en el qué hace un objeto, en lugar del cómo lo hace. """

# Encapsulamiento: 
""" Agrupar datos y métodos que operan sobre esos datos dentro de una clase """

# Herencia: 
""" Permite crear nuevas clases basadas en clases existentes, heredando sus atributos y métodos """

# Polimorfismo: 
""" Permite que diferentes clases puedan ser tratadas como instancias de una clase base común """

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular      # Atributo privado
        self.__saldo = saldo          # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito exitoso. Nuevo saldo: {self.__saldo}"
        else:
            return "Cantidad inválida para depósito."

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Retiro exitoso. Nuevo saldo: {self.__saldo}"
        else:
            return "Cantidad inválida para retiro o saldo insuficiente."

    def obtener_saldo(self):
        return self.__saldo
      
  # Metodos privados

    def __calcular_interes(self, tasa):
        return self.__saldo * tasa / 100