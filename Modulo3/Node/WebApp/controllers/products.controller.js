const Product = require("../models/products.js");

exports.getAllProducts = (req, res) => {
  Product.all()
    .then((products) => {
      res.render("products", {
        title: "Catalogo de Productos",
        products: products,
      });
    })
    .catch((err) => {
      console.error("Error retrieving products:", err);
      res.status(500).send("Internal Server Error");
    });
};

exports.getProductById = (req, res) => {
  const productId = req.params.id;
  Product.findById(productId)
    .then((product) => {
      if (product) {
        res.render("productDetail", {
          title: `Detalle de Producto - ${product.name}`,
          product: product,
        });
      } else {
        res.status(404).send("Producto No Encontrado");
      }
    })
    .catch((err) => {
      console.error("Error retrieving product:", err);
      res.status(500).send("Internal Server Error");
    });
};

exports.newProductForm = (req, res) => {
  res.render("newProduct", {
    title: "Agregar Nuevo Producto",
    product: null,
  });
};

exports.createNewProduct = (req, res) => {
  const productData = req.body;
  const params = req.params;
  const formData = req.formData;

  console.log("Received product data:", productData);
  console.log("Received params:", params);
  console.log("Received form data:", formData);
  Product.create(productData)
    .then((product) => {
      const newProductId = product.id;
      res.redirect(`/producto/${newProductId}`);
    })
    .catch((err) => {
      console.error("Error creating product:", err);
      res.status(500).send("Internal Server Error");
    });
};
