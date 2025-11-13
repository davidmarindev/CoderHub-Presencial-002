class Order:
    def __init__(self, customer_id, status="OPEN", note=""):
        self.id = None
        self.customer_id = customer_id
        self.status = status
        self.issued_at = None
        self.note = note
        self.subtotal = 0.0
        self.tax = 0.0
        self.discount_total = 0.0
        self.total = 0.0
        self.items = []
    
    def __repr__(self):
        return f"<Order(id={self.id}, customer_id={self.customer_id}, status={self.status}, total={self.total})>"
      
    @classmethod
    def all(cls, conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders")
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]
      
    @classmethod
    def new(cls, customer_id, status="OPEN", note=""):
        return cls(customer_id, status, note)
    
    @classmethod
    def create(cls, conn, order):
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO orders (customer_id, status, note, subtotal, tax, discount_total, total)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (order.customer_id, order.status, order.note, order.subtotal, order.tax, order.discount_total, order.total))
        conn.commit()
        order.id = cursor.lastrowid
        return order
      
    def add_item(self, item):
        self.items.append(item)
        
    def remove_item(self, item):
        self.items.remove(item)
        
    def list_items(self):
        return self.items
        
    def calculate_total(self):
      for item in self.items:
          self.total += item.unit_price * item.quantity
          
      return self.total