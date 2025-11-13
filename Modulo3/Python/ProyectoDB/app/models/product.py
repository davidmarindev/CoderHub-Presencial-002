class Product:
    def __init__(self, id, sku, name, category_id, price, cost_price, min_stock, current_stock, active=True, quantity=0):
        self.id = id
        self.sku = sku
        self.name = name
        self.category_id = category_id
        self.price = price
        self.cost_price = cost_price
        self.min_stock = min_stock
        self.current_stock = current_stock
        self.active = active

    def __repr__(self):
        return f"Product(id={self.id}, sku={self.sku}, name='{self.name}', price={self.price}, cost_price={self.cost_price}, current_stock={self.current_stock})"

    # Leer productos desde la base de datos
    # Crear producto
    # Leer producto
    # Actualizar producto
    # Eliminar producto
    
    # Metodos de clase
    @classmethod
    def all(cls, conn):
        print("Listado de productos:")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        for row in rows:
            product = cls(*row)
            print("Producto:", product)

    @classmethod
    def create(cls, conn, product):
        print("Creando producto:")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO products (sku, name, category_id, price, cost_price, min_stock, current_stock)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (product.sku, product.name, product.category_id, product.price, product.cost_price, product.min_stock, product.current_stock))
        conn.commit()
        return product

    @classmethod
    def find(cls, conn, product_id):
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM products WHERE id = ? OR sku = ?
        """, (product_id, product_id))
        row = cursor.fetchone()
        if row:
            return cls(*row)
        return None

    @classmethod
    def update(cls, conn, product):
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE products
            SET name = ?, cost_price = ?, price = ?, active = ?, min_stock = ?
            WHERE id = ?
        """, (product.name, product.cost_price, product.price, product.active, product.id))
        conn.commit()

    @classmethod
    def delete(cls, conn, product_id):
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM products WHERE id = ?
        """, (product_id,))
        conn.commit()
        
        print(f"Producto con ID {product_id} eliminado.")
        
    @classmethod
    def search_by_attribute(cls, conn, attribute, value):
        cursor = conn.cursor()
        query = f"SELECT * FROM products WHERE {attribute} = ?"
        cursor.execute(query, (value,))
        rows = cursor.fetchall()
        products = [cls(*row) for row in rows]

        return products

    # Metodos de instancia
    
    def calculate_margin(self):
        if self.cost_price == 0:
            return 0
        margin = ((self.price - self.cost_price) / self.cost_price) * 100

        return margin