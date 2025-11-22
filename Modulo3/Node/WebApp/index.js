const express = require("express");
const app = express();
const path = require("node:path");
const port = 3000;
const ProductController = require("./controllers/products.controller.js");
const db = require("./db.js");

app.use(express.static(path.join(__dirname, "public")));

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Rutas
app.get("/", (req, res) => {
  res.render("index", {
    title: "Home Web Page",
    user: { name: "David", email: "david@example.com" },
  });
});
app.get("/catalogo", ProductController.getAllProducts);
app.get("/producto/:id", ProductController.getProductById);
app.get("/nuevo-producto", ProductController.newProductForm);
app.post("/producto", ProductController.createNewProduct);

// Validar la conexión a la base de datos

db.serialize(() => {
  db.each("SELECT name FROM sqlite_master WHERE type='table'", (err, row) => {
    if (err) {
      console.error("Error retrieving tables:", err.message);
    } else {
      console.log("Table found:", row.name);
    }
  });
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});

// Server
// Rutas
// Controladores
// Modelos
// Vistas

// Flujo actual de petición-respuesta

// 1. Recibimos una petición HTTP en una ruta específica.
// 2. La ruta invoca un controlador correspondiente.
// 3. El controlador interactúa con el modelo para obtener o manipular datos.
// 4. El modelo se comunica con la base de datos para realizar operaciones CRUD.
// 5. Los datos obtenidos se devuelven al controlador.
// 6. El controlador renderiza una vista con los datos y envía la respuesta al cliente.
// 7. El cliente recibe la respuesta y muestra la vista renderizada.

// HTTP methods: GET, POST, PUT, DELETE
