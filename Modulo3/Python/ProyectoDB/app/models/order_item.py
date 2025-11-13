class OrderItem:
    def __init__(self, order_id, product_id, quantity, unit_price):
        self.id = None
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price
        
    def __repr__(self):
        return f"<OrderItem(id={self.id}, order_id={self.order_id}, product_id={self.product_id}, quantity={self.quantity}, unit_price={self.unit_price})>"
      
    @classmethod
    def create(cls, conn, order_item):
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO order_items (order_id, product_id, quantity, unit_price)
            VALUES (?, ?, ?, ?)
        """, (order_item.order_id, order_item.product_id, order_item.quantity, order_item.unit_price))
        conn.commit()
        order_item.id = cursor.lastrowid
        return order_item