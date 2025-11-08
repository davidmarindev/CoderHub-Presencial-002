PRAGMA foreign_keys = ON;

-- =========================
-- CORE
-- =========================
CREATE TABLE IF NOT EXISTS categories (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  name       TEXT NOT NULL UNIQUE,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS suppliers (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  name       TEXT NOT NULL,
  tax_id     TEXT,
  phone      TEXT,
  email      TEXT,
  address    TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(name)
);

CREATE TABLE IF NOT EXISTS products (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  sku           TEXT NOT NULL UNIQUE,
  name          TEXT NOT NULL,
  category_id   INTEGER,
  price         REAL NOT NULL DEFAULT 0,     -- precio de venta sugerido
  cost_price    REAL NOT NULL DEFAULT 0,     -- costo de referencia
  min_stock     INTEGER NOT NULL DEFAULT 0,
  current_stock INTEGER NOT NULL DEFAULT 0,  -- stock actual mantenido por triggers
  active        INTEGER NOT NULL DEFAULT 1,  -- 1=true, 0=false
  created_at    TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_products_category ON products(category_id);
CREATE INDEX IF NOT EXISTS idx_products_active   ON products(active);

-- Historial de movimientos (entradas/salidas)
CREATE TABLE IF NOT EXISTS stock_movements (
  id             INTEGER PRIMARY KEY AUTOINCREMENT,
  product_id     INTEGER NOT NULL,
  movement_type  TEXT NOT NULL CHECK (movement_type IN ('IN','OUT')),
  quantity       INTEGER NOT NULL CHECK (quantity > 0),
  unit_cost      REAL,                         -- costo por unidad (usual en IN)
  unit_price     REAL,                         -- precio por unidad (usual en OUT)
  note           TEXT,
  created_at     TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  supplier_id    INTEGER,                      -- opcional para IN
  order_id       INTEGER,                      -- opcional para OUT (ref a orders)
  FOREIGN KEY (product_id) REFERENCES products(id)   ON DELETE RESTRICT,
  FOREIGN KEY (supplier_id) REFERENCES suppliers(id) ON DELETE SET NULL
  -- FOREIGN KEY (order_id) se define abajo cuando exista 'orders'
);

CREATE INDEX IF NOT EXISTS idx_movements_product  ON stock_movements(product_id);
CREATE INDEX IF NOT EXISTS idx_movements_type     ON stock_movements(movement_type);
CREATE INDEX IF NOT EXISTS idx_movements_supplier ON stock_movements(supplier_id);
CREATE INDEX IF NOT EXISTS idx_movements_created  ON stock_movements(created_at);

-- =========================
-- VENTAS
-- =========================
CREATE TABLE IF NOT EXISTS customers (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  name       TEXT NOT NULL,
  phone      TEXT,
  email      TEXT,
  address    TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS orders (
  id             INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id    INTEGER,
  status         TEXT NOT NULL DEFAULT 'OPEN'
                 CHECK (status IN ('OPEN','PAID','CANCELLED','PARTIAL')),
  issued_at      TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  note           TEXT,
  -- Totales (si prefieres calcular en app, puedes mantenerlos en 0)
  subtotal       REAL NOT NULL DEFAULT 0,
  tax            REAL NOT NULL DEFAULT 0,
  discount_total REAL NOT NULL DEFAULT 0,
  total          REAL NOT NULL DEFAULT 0,
  FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_orders_customer ON orders(customer_id);
CREATE INDEX IF NOT EXISTS idx_orders_status   ON orders(status);
CREATE INDEX IF NOT EXISTS idx_orders_issued   ON orders(issued_at);

CREATE TABLE IF NOT EXISTS order_items (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  order_id    INTEGER NOT NULL,
  product_id  INTEGER NOT NULL,
  quantity    INTEGER NOT NULL CHECK (quantity > 0),
  unit_price  REAL NOT NULL,
  discount    REAL NOT NULL DEFAULT 0,   -- monto de descuento (unitario o total por ítem según tu regla)
  tax_rate    REAL NOT NULL DEFAULT 0,   -- 0..1
  created_at  TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (order_id)   REFERENCES orders(id)   ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_order_items_order   ON order_items(order_id);
CREATE INDEX IF NOT EXISTS idx_order_items_product ON order_items(product_id);

CREATE TABLE IF NOT EXISTS payment_methods (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  code       TEXT NOT NULL UNIQUE,  -- 'CASH','CARD','BANK','ZELLE', etc.
  name       TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS payments (
  id                INTEGER PRIMARY KEY AUTOINCREMENT,
  order_id          INTEGER NOT NULL,
  payment_method_id INTEGER NOT NULL,
  amount            REAL NOT NULL CHECK (amount > 0),
  paid_at           TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  reference         TEXT,
  note              TEXT,
  FOREIGN KEY (order_id)          REFERENCES orders(id)          ON DELETE CASCADE,
  FOREIGN KEY (payment_method_id) REFERENCES payment_methods(id) ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_payments_order  ON payments(order_id);
CREATE INDEX IF NOT EXISTS idx_payments_method ON payments(payment_method_id);
CREATE INDEX IF NOT EXISTS idx_payments_paid   ON payments(paid_at);