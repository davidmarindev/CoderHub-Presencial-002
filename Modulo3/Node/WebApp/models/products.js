const db = require("../db.js");

class Product {
  constructor(id, name, price, category) {
    this.id = id;
    this.name = name;
    this.price = price;
    this.category = category;
  }

  static all() {
    return new Promise((resolve, reject) => {
      db.all("SELECT * FROM Products", (err, rows) => {
        if (err) {
          reject(err);
        } else {
          resolve(rows);
        }
      });
    });
  }

  static findById(id) {
    return new Promise((resolve, reject) => {
      db.get("SELECT * FROM Products WHERE ProductID = ?", [id], (err, row) => {
        if (err) {
          reject(err);
        } else {
          resolve(row);
        }
      });
    });
  }

  static create(productData) {
    return new Promise((resolve, reject) => {
      const {
        name,
        price,
        stock,
        categoryId,
        supplierId,
        quantityPerUnit,
        unitsOnOrder,
      } = productData;
      db.run(
        "INSERT INTO Products (ProductName, UnitPrice, UnitsInStock, CategoryID, SupplierID, QuantityPerUnit, UnitsOnOrder) VALUES (?, ?, ?, ?, ?, ?, ?)",
        [
          name,
          price,
          stock,
          categoryId,
          supplierId,
          quantityPerUnit,
          unitsOnOrder,
        ],
        function (err) {
          if (err) {
            reject(err);
          } else {
            resolve({ id: this.lastID, ...productData });
          }
        }
      );
    });
  }
}

module.exports = Product;
