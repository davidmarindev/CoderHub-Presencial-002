const db = require("../db");

class Product {
  static getAll(callback) {
    const sql = "SELECT * FROM products";
    db.all(sql, [], (err, rows) => {
      if (err) {
        return callback(err);
      }
      callback(null, rows);
    });
  }

  static getById(id, callback) {
    const sql = "SELECT * FROM products WHERE id = ?";
    db.get(sql, [id], (err, row) => {
      if (err) {
        return callback(err);
      }
      callback(null, row);
    });
  }

  static create(product, callback) {
    const sql =
      "INSERT INTO products (name, price, description) VALUES (?, ?, ?)";
    const params = [product.name, product.price, product.description];
    db.run(sql, params, (err) => {
      if (err) {
        return callback(err);
      }

      callback(null, { id: this.lastID, ...product });
    });
  }

  static update(id, product, callback) {
    const sql =
      "UPDATE products SET name = ?, price = ?, description = ? WHERE id = ?";
    const params = [product.name, product.price, product.description, id];
    db.run(sql, params, function (err) {
      if (err) {
        return callback(err);
      }
      callback(null, { id, ...product });
    });
  }

  static delete(id, callback) {
    const sql = "DELETE FROM products WHERE id = ?";
    db.run(sql, [id], function (err) {
      if (err) {
        return callback(err);
      }
      callback(null);
    });
  }
}

module.exports = Product;
