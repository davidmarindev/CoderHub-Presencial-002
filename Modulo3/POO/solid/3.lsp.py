# Liskov Substitution Principle (LSP)

class Ave:
  def fly(self):
    print("Flying")
  
  def walk(self):
    print("Walking")

  def swing(self):
    print("Swinging")

class AveNoVoladora(Ave):
  def fly(self):
    raise Exception("Ostriches can't fly")

  def walk(self):
    print("Walking on the ground")
  
  def swing(self):
    print("Swinging")

class AveVoladora(Ave ):
  def fly(self):
    print("Flying")

  def walk(self):
    print("Walking on the air")

class Pinguino(AveNoVoladora):
  def walk(self):
    return super().walk()
  
  def swing(self):
    return super().swing()
  
class Loro(AveVoladora):
  def fly(self):
    return super().fly()
  
  def walk(self):
    return super().walk()
  
  def swing(self):
    raise Exception("Parrots don't swing")

