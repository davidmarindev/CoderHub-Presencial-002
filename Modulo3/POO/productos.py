class Producto:
    def __init__(self, nombre, precio, categoria, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Categoría: {self.categoria}"
      
    def calcular_descuento(self):
        descuento = self.precio * (10 / 100)
        precio_final = self.precio - descuento
        print(f"Descuento aplicado: {descuento}, porcentaje: 10%")
        return precio_final

class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, categoria, marca, modelo, garantia, stock=0):
        super().__init__(nombre, precio, categoria, stock)
        self.marca = marca
        self.modelo = modelo
        self.garantia = garantia
        self.porcentaje_descuento = 15  # Descuento especial para electrónicos

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Marca: {self.marca}, Modelo: {self.modelo}"
    
    def calcular_descuento(self):
        descuento = self.precio * (self.porcentaje_descuento / 100)
        precio_final = self.precio - descuento
        print(f"Descuento aplicado: {descuento}, porcentaje: {self.porcentaje_descuento}%")
        return precio_final
      
class ProductoRopa(Producto):
    def __init__(self, nombre, precio, categoria, talla, color, stock=0):
        super().__init__(nombre, precio, categoria, stock)
        self.talla = talla
        self.color = color
        self.porcentaje_descuento = 20  # Descuento especial para ropa

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Talla: {self.talla}, Color: {self.color}"
    
    def calcular_descuento(self):
        descuento = self.precio * (self.porcentaje_descuento / 100)
        precio_final = self.precio - descuento
        print(f"Descuento aplicado: {descuento}, porcentaje: {self.porcentaje_descuento}%")
        return precio_final
      
class ProductoAlimento(Producto):
    def __init__(self, nombre, precio, categoria, fecha_caducidad, stock=0):
        super().__init__(nombre, precio, categoria, stock)
        self.fecha_caducidad = fecha_caducidad

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Fecha de Caducidad: {self.fecha_caducidad}"
      
      
laptop = ProductoElectronico("Laptop", 1500, "Electrónica", "Dell", "XPS 13", "2 años", 10)
camiseta = ProductoRopa("Camiseta", 25, "Ropa", "M", "Azul", 50)
manzanas = ProductoAlimento("Manzanas", 3, "Alimentos", "2024-12-31", 100)

print(laptop.calcular_descuento())
print(camiseta.calcular_descuento())
print(manzanas.calcular_descuento())