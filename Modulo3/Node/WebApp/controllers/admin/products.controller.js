const Product = require("../../models/products.js");

exports.getAllProducts = (req, res) => {
  Product.all()
    .then((products) => {
      res.render("admin/products", {
        title: "Catalogo de Productos",
        products: products,
      });
    })
    .catch((err) => {
      console.error("Error retrieving products:", err);
      res.status(500).send("Internal Server Error");
    });
};

exports.editProduct = (req, res) => {
  const productId = req.params.id;
  Product.findById(productId)
    .then((product) => {
      if (product) {
        console.log("Editing product:", product);
        res.render("newProduct", {
          title: `Editar Producto - ${product.ProductName}`,
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

exports.updateProduct = (req, res) => {
  const productId = req.params.id;
  const productData = req.body;

  Product.updateById(productId, productData)
    .then(() => {
      res.redirect("/admin/productos");
    })
    .catch((err) => {
      console.error("Error updating product:", err);
      res.status(500).send("Internal Server Error");
    });
};

exports.deleteProduct = (req, res) => {
  const productId = req.params.id;
  Product.deleteById(productId)
    .then(() => {
      res.redirect("/admin/productos");
    })
    .catch((err) => {
      console.error("Error deleting product:", err);
      res.status(500).send("Internal Server Error");
    });
};
