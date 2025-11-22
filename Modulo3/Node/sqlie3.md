## 🚀 Instalación de SQLite3

Para instalar SQLite3 en tu proyecto de Node.js, utiliza el siguiente comando:

```bash
npm install sqlite3
```

## 📦 Uso Básico de SQLite3 en Node.js

```javascript
const sqlite3 = require("sqlite3").verbose();
const db = new sqlite3.Database(":memory:");

// Crear una tabla
db.serialize(() => {
  db.run("CREATE TABLE user (id INT, name TEXT)");

  // Insertar datos
  const stmt = db.prepare("INSERT INTO user VALUES (?, ?)");
  stmt.run(1, "John Doe");
  stmt.finalize();

  // Consultar datos
  db.all("SELECT * FROM user", [], (err, rows) => {
    if (err) {
      throw err;
    }
    rows.forEach((row) => {
      console.log(row);
    });
  });
  // Otra forma de consultar datos
  db.each("SELECT id, name FROM user", (err, row) => {
    if (err) {
      console.error(err);
    } else {
      console.log(`${row.id}: ${row.name}`);
    }
      });
    });
    ```

  db.each("SELECT id, name FROM user", (err, row) => {
    if (err) {
      console.error(err);
    } else {
      console.log(`${row.id}: ${row.name}`);
    }
  });
});

// Cerrar la conexión
db.close();
```
