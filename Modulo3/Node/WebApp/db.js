const sqlite3 = require("sqlite3").verbose();
const path = require("node:path");

const dbPath = path.join(__dirname, "./db/northwind.db");
const db = new sqlite3.Database(dbPath);

module.exports = db;
