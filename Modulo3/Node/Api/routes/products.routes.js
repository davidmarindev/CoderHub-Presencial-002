const express = require("express");
const router = express.Router();
const ProductController = require("../controllers/products.controller.js");

// Metodos

router.get("/", ProductController.getAllProducts);
router.post("/", ProductController.createProduct);
router.get("/:id", ProductController.getProductById);
router.put("/:id/edit", ProductController.updateProduct);
router.delete("/:id", ProductController.deleteProduct);

module.exports = router;
