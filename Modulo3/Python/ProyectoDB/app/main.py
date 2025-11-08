from db import create_connection
from models.product import Product

def main():
    conn = create_connection()
    if conn:
        print("Conexión a la base de datos establecida.")
    else:
        print("Error al conectar a la base de datos.")

    while True:
        print()
        print("Biendvenido al sistema de inventario")
        print()
        
        print("Menu de opciones:")
        print()
        print("Seleccione el módulo al que desea acceder indicando el numero.:")
        
        print("1. Modulo de Productos:")
        print("2. Modulo de Ventas:")
        print("3. Modulo de Compras:")
        print("4. Modulo de Proveedores:")
        print("5. Modulo de Categorias:")
        print("6. Modulo de Clientes:")
        print("7. Salir")
        
        option = input("Seleccione una opción: ")
        print()
        
        match option:
            case "1":
                print("Accediendo al módulo de Productos...")
                print("1. Listar productos")
                print("2. Buscar productos por ID o SKU")
                print("3. Agregar producto")
                print("4. Actualizar producto")
                print("5. Eliminar producto")
                print("6. Volver al menú principal")
                
                product_option = input("Seleccione una opción de productos: ")
                print()
                
                match product_option:
                    case "1":
                        Product.all(conn)
                    case "2":
                        id = input("Ingrese el ID o SKU del producto: ")
                        product = Product.find(conn, id)
                        
                        if product:
                            print("Producto encontrado:", product)
                        else:
                            print("Producto no encontrado.")
                    case "3":
                        sku = input("Ingrese el SKU del producto: ")
                        name = input("Ingrese el nombre del producto: ")
                        category_id = input("Ingrese el ID de la categoría: ")
                        price = float(input("Ingrese el precio del producto: "))
                        cost_price = float(input("Ingrese el precio de costo del producto: "))
                        min_stock = int(input("Ingrese el stock mínimo del producto: "))
                        current_stock = int(input("Ingrese el stock actual del producto: "))
                        product = Product(None, sku, name, category_id, price, cost_price, min_stock, current_stock)
                        Product.create(conn, product)
                    case "4":
                        id = input("Ingrese el ID del producto a actualizar: ")
                        product = Product.find(conn, id)
                        if product:
                            print("Producto encontrado:", product)
                            # Aquí se pueden solicitar los nuevos valores para actualizar el producto
                            product.name = input("Ingrese el nuevo nombre del producto: ")
                            product.price = float(input("Ingrese el nuevo precio del producto: "))
                            Product.update(conn, product)
                        else:
                            print("Producto no encontrado.")
                    case "5":
                        id = input("Ingrese el ID del producto a eliminar: ")
                        product = Product.find(conn, id)
                        if not product:
                            print("Producto no encontrado.")
                        else:
                            Product.delete(conn, id)
                    case "6":
                        continue
                    case _:
                        print("Opción no válida en el módulo de Productos.")
            case "2":
                print("Accediendo al módulo de Ventas...")
            case "3":
                print("Accediendo al módulo de Compras...")
            case "4":
                print("Accediendo al módulo de Proveedores...")
            case "5":
                print("Accediendo al módulo de Categorias...")
            case "6":
                print("Accediendo al módulo de Clientes...")
            case "7":
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")
                print()

if __name__ == "__main__":
    main()