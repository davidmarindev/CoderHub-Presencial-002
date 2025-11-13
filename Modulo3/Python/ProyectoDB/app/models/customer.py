class Customer:
    def __init__(self, name, document_number, phone, email, address, id=None, created_at=None):
        self.id = id
        self.name = name
        self.document_number = document_number
        self.phone = phone
        self.email = email
        self.address = address
        self.created_at = created_at

    def __repr__(self):
        return f"<Customer(id={self.id}, name={self.name}, phone={self.phone}, document_number={self.document_number}, email={self.email}, address={self.address})>"

    @classmethod
    def all(cls, conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()
        print("Rows", rows)
        print("Listado de clientes:")
        for row in rows:
            print("Cliente:", row)
      
    @classmethod
    def find_or_create(cls, conn, document_number):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE document_number = ?", (document_number,))
        row = cursor.fetchone()
        if row:
            return cls(*row)
        else:
            print("Cliente no encontrado. Por favor, ingrese los detalles del nuevo cliente.")
            print()
            name = input("Ingrese el nombre del cliente: ")
            phone = input("Ingrese el teléfono del cliente: ")
            email = input("Ingrese el correo electrónico del cliente: ")
            address = input("Ingrese la dirección del cliente: ")
            cursor.execute("INSERT INTO customers (name, document_number, phone, email, address) VALUES (?, ?, ?, ?, ?)",
                           (name, document_number, phone, email, address))
            conn.commit()
            new_id = cursor.lastrowid
            return cls(new_id, name, document_number, phone, email, address)
     
    def show_details(self):
        print(f"Customer Details:\nID: {self.id}\nName: {self.name}\nDocument Number: {self.document_number}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}")