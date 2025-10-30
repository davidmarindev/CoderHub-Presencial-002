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
        return self.__saldo * tasa


class Cocktail:
    def __init__(self, nombre, base, modificador, precio, ingredientes):
        self.nombre = nombre
        self.base = base
        self.modificador = modificador
        self.precio = precio
        self.ingredientes = ingredientes

    def mezclar(self):
        return f"Mezclando los ingredientes para el cóctel {self.nombre}: {', '.join(self.ingredientes)}"
    
    def mostrar_receta(self):
        return f"Receta del cóctel {self.nombre}:\nBase: {self.base}\nModificador: {self.modificador}\nPrecio: ${self.precio}\nIngredientes: {', '.join(self.ingredientes)}"

class CocktailAlcoholico(Cocktail):
    def __init__(self, nombre, base, modificador, precio, ingredientes, grado_alcohol):
        super().__init__(nombre, base, modificador, precio, ingredientes)
        self.grado_alcohol = grado_alcohol

    def servir(self):
        return f"Sirviendo el cóctel alcohólico {self.nombre} con {self.grado_alcohol}% de alcohol."
    
    def indicar_grado_alcohol(self):
        return f"El cóctel {self.nombre} tiene un grado de alcohol de {self.grado_alcohol}%."
    
class CocktailSinAlcohol(Cocktail):
    def __init__(self, nombre, base, modificador, precio, ingredientes, ingrediente_especial):
        super().__init__(nombre, base, modificador, precio, ingredientes)
        self.ingrediente_especial = ingrediente_especial

    def servir(self):
        return f"Sirviendo el cóctel sin alcohol {self.nombre}."

    def indicar_ingrediente_especial(self):
        return f"El cóctel {self.nombre} tiene como ingrediente especial {self.ingrediente_especial}."
    

mojito = CocktailAlcoholico(
    nombre="Mojito",
    base="Ron",
    modificador="Azúcar",
    precio=8.50,
    ingredientes=["Ron", "Azúcar", "Lima", "Hierbabuena", "Soda"],
    grado_alcohol=13
)

pina_colada = CocktailSinAlcohol(
    nombre="Piña Colada",
    base="Jugo de Piña",
    modificador="Crema de Coco",
    precio=7.00,
    ingredientes=["Jugo de Piña", "Crema de Coco", "Hielo", "Azúcar", "Leche Condensada"],
    ingrediente_especial="Crema de Coco"
)

print(mojito.nombre)
print(pina_colada.nombre)

print(pina_colada.mostrar_receta())
print(mojito.mostrar_receta())

print(mojito.indicar_grado_alcohol())

print(type("Hola"))
print(type(123))
print(type(mojito))

print(isinstance(mojito, Cocktail))
print(isinstance(pina_colada, CocktailAlcoholico))
print(isinstance(pina_colada, Cocktail))