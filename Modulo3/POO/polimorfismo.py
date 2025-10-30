class Animal:
  def __init__(self, name):
    self.name = name

  def eat(self):
    print(f"{self.name} is eating.")

class Dog(Animal):
  def eat(self):
    print(f"{self.name} is eating meat.")

class Cat(Animal):
  def eat(self):
    print(f"{self.name} is eating fish.")
    
class Horse(Animal):
  def eat(self):
    print(f"{self.name} is eating hay.")


animals = [Dog("Buddy"), Cat("Whiskers"), Horse("Charlie")]

for animal in animals:
  animal.eat()

class Absenteeism:
  def __init__(self, employee_name, days_absent):
    self.employee_name = employee_name
    self.days_absent = days_absent

class LicensedAbsenteeism(Absenteeism):
  def __init__(self, employee_name, days_absent, license_type):
    super().__init__(employee_name, days_absent)
    self.license_type = license_type
  
  def is_paid(self):
    print("Every licensed absenteeism is paid.")

class UnlicensedAbsenteeism(Absenteeism):
  def __init__(self, employee_name, days_absent, reason):
    super().__init__(employee_name, days_absent)
    self.reason = reason

  def is_paid(self):
    print("Unlicensed absenteeism is not paid.")

class VacationAbsenteeism(Absenteeism):
  def __init__(self, employee_name, days_absent, vacation_start_date):
    super().__init__(employee_name, days_absent)
    self.vacation_start_date = vacation_start_date
    
  def is_paid(self):
    print("Vacation absenteeism is paid.")

#Ejercicio Empleados.

class Employee:
  def __init__(self, name, position):
    self.name = name
    self.position = position

  def calculate_salary(self):
    pass

class FullTimeEmployee(Employee):
  def __init__(self, name, position, salary):
    super().__init__(name, position)
    self.salary = salary

  def calculate_salary(self):
    return self.salary

class PartTimeEmployee(Employee):
  def __init__(self, name, position, hourly_rate, hours_worked):
    super().__init__(name, position)
    self.hourly_rate = hourly_rate
    self.hours_worked = hours_worked

  def calculate_salary(self):
    return self.hourly_rate * self.hours_worked
  
employees = [
  FullTimeEmployee("Alice", "Developer", 60000),
  PartTimeEmployee("Bob", "Designer", 30, 120),
  PartTimeEmployee("Charlie", "Tester", 25, 100)
]

# Metodos de clase para saber si es una instancia.

# for emp in employees:
#   print(f"{emp.name} earns: ${emp.calculate_salary()}")
#   if isinstance(emp, FullTimeEmployee):
#     print(f"{emp.name} is a full-time employee.")
#   elif isinstance(emp, PartTimeEmployee):
#     print(f"{emp.name} is a part-time employee.")

emp = employees[0]
print(isinstance(emp, PartTimeEmployee))  # True
print(issubclass(emp.__class__, Employee))  # True