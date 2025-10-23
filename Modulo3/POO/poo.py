# Programación Orientada a Objetos (POO)

# Componentes principales de la POO:

# Clase -> Plantilla o molde para crear objetos
# Objeto -> Instancia de una clase(Entidad)
# Atributos -> Características o propiedades de una clase u objeto
# Métodos -> Funciones definidas dentro de una clase que describen el comportamiento de un objeto
# Constructor -> Método especial que se llama al crear un objeto y se utiliza para inicializar atributos

class Car:
  # Constructor
  def __init__(self, name, model, year, brand, color):
      self.name = name         # Atributo
      self.model = model        # Atributo
      self.year = year          # Atributo
      self.brand = brand        # Atributo
      self.color = color        # Atributo

  # Métodos
  def start_engine(self):
      return f"The engine of the {self.name} {self.year} {self.brand} {self.model} is starting."

  def stop_engine(self):
      return f"The engine of the {self.name} {self.year} {self.brand} {self.model} is stopping."
    
  def paint(self, new_color):
      self.color = new_color
      return f"The {self.name} has been painted {self.color}."

# Crear un objeto (instancia de la clase Car)
car_one = Car("Mustang", "GT", 2021, "Ford" , "Red")
car_two = Car("Civic", "EX", 2020, "Honda", "Blue")

print("Car One:", car_one.color)
print("Car Two:", car_two.start_engine())
print(car_one.paint("Black"))
print("Car One New Color:", car_one.color)
car_one.color = "Green"  # Modificando el atributo directamente

# Metodos de instancia
# Metodos de clase 
# Metodos estaticos

class Person:
  def __init__(self, name, lastname, email, age):
      self.name = name
      self.lastname = lastname
      self.email = email
      self.age = age
  
  def __str__(self):
      return f"Person(Name: {self.name}, Lastname: {self.lastname}, Email: {self.email}, Age: {self.age})"
    
  def is_adult(self):
      return self.age >= 18


personas = [
   { "name": "Juan", "lastname": "Perez", "email": "juan.perez@example.com", "age": 28 },
   { "name": "Maria", "lastname": "Gomez", "email": "maria.gomez@example.com", "age": 15 },
   { "name": "Carlos", "lastname": "Lopez", "email": "carlos.lopez@example.com", "age": 30 }
]

personas_objects = []

for p in personas:
    persona = Person(p["name"], p["lastname"], p["email"], p["age"])
    personas_objects.append(persona)
    
for persona in personas_objects:
    if persona.is_adult():
        print(f"Persona {personas_objects.index(persona) + 1}: {persona}")
