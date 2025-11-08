SELECT EmployeeID, FirstName, TitleOfCourtesy FROM employees;

SELECT * FROM employees WHERE Country = "USA";

SELECT * FROM employees WHERE EmployeeID = 8;

UPDATE employees SET "Country" = "VE";

SELECT * FROM "order details";

DELETE FROM "order details" WHERE OrderID = 100;

-- Filtros con operadores

SELECT * FROM products WHERE UnitPrice < 65;

SELECT * FROM products WHERE UnitsInStock < 5;

SELECT * FROM products WHERE UnitPrice BETWEEN 5 AND 20;

SELECT * FROM employees WHERE HireDate BETWEEN "2012-01-01" AND "2012-12-31" ;

SELECT * FROM products WHERE UnitPrice > 20 AND UnitsInStock > 100;

SELECT * FROM customers WHERE Fax IS NULL;

SELECT * FROM customers WHERE Fax IS NOT NULL:

SELECT COUNT(*) FROM customers ;

SELECT * FROM products WHERE ProductID IN (1, 10, 25);§

SELECT * FROM products WHERE ProductID NOT IN (1, 10, 25);

SELECT * FROM customers WHERE Country = "Germany" OR Country = "Spain";

SELECT * FROM Suppliers ORDER BY CompanyName DESC;

SELECT * FROM Products ORDER BY UnitPrice ASC;

SELECT * FROM Products ORDER BY UnitPrice ASC LIMIT 1; 

SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
ORDER BY Country DESC;

SELECT * FROM products WHERE ProductName LIKE '%u';