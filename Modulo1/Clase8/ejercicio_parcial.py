# Sistema de gestión de ventas por consola

# Desarrollar un sistema de gestion de inventario por consola que permita:

# 1. Agregar productos al inventario. (Nombre, precio, cantidad, Identificador)
# 2. Consultar productos dispinibles en el inventario.
# 3. Modificar productos del inventario pero solo precio y stock.
# 4. Eliminar productos del inventario.
# 5. Crear funcion para calcular iva de un producto.
# 6. Crear para calcular descuento de un producto, debe recibir un porcentaje y el precio del producto.
# 7. Calcular el total de ventas del inventario del mes.)

productos = []
ventas = []

def agregar_producto(nombre, precio, cantidad, identificador):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "identificador": identificador
    }

    productos.append(producto)
    print(f"Producto '{nombre}' agregado al inventario.")

def mostrar_productos():
    if not productos:
        print("No hay productos en el inventario.")
        return
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}, Identificador: {producto['identificador']}")
        
def buscar_producto(identificador):
    for producto in productos:
        if producto['identificador'] == identificador:
            return producto
    return None
  
def calcular_iva(producto, tasa_iva):
    iva = producto['precio'] * (tasa_iva / 100)
    total_con_iva = producto['precio'] + iva
    print(f"IVA del producto '{producto['nombre']}': {iva:.2f}, Total con IVA: {total_con_iva:.2f}")
    
while True:
    print("\nSistema de Gestión de Inventario")
    print("1. Agregar producto")
    print("2. Consultar productos")
    print("3. Modificar producto")
    print("4. Eliminar producto")
    print("5. Calcular IVA de un producto")
    print("6. Calcular descuento de un producto")
    print("7. Calcular total de ventas del mes")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
      case "1":
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        identificador = input("Ingrese el identificador del producto: ")
        agregar_producto(nombre, precio, cantidad, identificador)

      case "2":
        print("Productos disponibles en el inventario:")
        mostrar_productos()
      
      case "3":
        print("Modificar producto")
        
      case "4":
        print("Eliminar producto")
      
      case "5":
        print("Calcular IVA de un producto")
        identificador = input("Ingrese el identificador del producto: ")
        producto = buscar_producto(identificador)
        if producto:
            calcular_iva(producto, 16)
        else:
            print("Producto no encontrado.")
      
      case "6":
        print("Calcular descuento de un producto")
      
      case "7":
        print("Calcular total de ventas del mes")
        
      case "8":
        print("Saliendo del sistema de gestión de inventario.")
        break

      case _:
        print("Opción no válida, intente de nuevo.")

    