const express = require("express");
const router = express.Router();
const productsRoutes = require("./products.routes.js");

router.get("/status", (req, res) => {
  res.json({ status: "API is running" });
});

router.use("/products", productsRoutes);

module.exports = router;
