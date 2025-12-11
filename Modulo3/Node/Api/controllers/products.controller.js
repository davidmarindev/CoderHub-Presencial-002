const Product = require("../models/product.js");

const validateExistance = (productId, res) => {
  // Validate if product exists before updating
  Product.getById(productId, (err, existingProduct) => {
    if (err) {
      return res.status(404).json({ error: "Product not found" });
    }
    if (!existingProduct) {
      return res.status(404).json({ error: "Product not found" });
    }
  });
};

const getAllProducts = (req, res) => {
  Product.getAll((err, products) => {
    if (err) {
      return res.status(500).json({ error: "Failed to retrieve products" });
    }
    res.json(products);
  });
};

const getProductById = (req, res) => {
  const productId = parseInt(req.params.id);
  Product.getById(productId, (err, product) => {
    if (err) {
      return res.status(500).json({ error: "Failed to retrieve product" });
    }
    if (!product) {
      return res.status(404).json({ error: "Product not found" });
    }
    res.json(product);
  });
};

const createProduct = (req, res) => {
  const newProduct = {
    name: req.body.name,
    price: req.body.price,
    description: req.body.description,
  };
  Product.create(newProduct, (err, createdProduct) => {
    if (err) {
      return res.status(500).json({ error: "Failed to create product" });
    }
    res.status(201).json(createdProduct);
  });
};

const updateProduct = (req, res) => {
  const productId = parseInt(req.params.id);
  validateExistance(productId, res);

  const updatedProduct = {
    name: req.body.name,
    price: req.body.price,
    description: req.body.description,
  };
  Product.update(productId, updatedProduct, (err, product) => {
    if (err) {
      return res.status(500).json({ error: "Failed to update product" });
    }
    res.json(product);
  });
};

const deleteProduct = (req, res) => {
  const productId = parseInt(req.params.id);
  validateExistance(productId, res);

  Product.delete(productId, (err) => {
    if (err) {
      return res.status(500).json({ error: "Failed to delete product" });
    }
    res.status(204).send();
  });
};

module.exports = {
  getAllProducts,
  getProductById,
  createProduct,
  updateProduct,
  deleteProduct,
};
