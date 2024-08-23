SELECT o.OrderID, c.CustomerID, c.CustomerName, c.Country
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
ORDER BY o.OrderID;
-- 2 --
SELECT c.Country, COUNT(o.OrderID) AS Ordered
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
GROUP BY c.Country
ORDER BY Ordered DESC;
-- 3 --
SELECT od.ProductID, p.ProductName, od.Quantity, p.Price
FROM OrderDetails od
JOIN Products p ON od.ProductID = p.ProductID
WHERE od.OrderID = 10248;
-- 4 --
SELECT od.OrderID, SUM(od.Quantity * p.Price) AS TotalAmount
FROM OrderDetails od
JOIN Products p ON od.ProductID = p.ProductID
WHERE od.OrderID = 10248
GROUP BY od.OrderID;
-- 5 --
SELECT o.OrderID, SUM(od.Quantity * p.Price) AS TotalAmount
FROM Orders o
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE o.OrderDate = '1996-08-01'
GROUP BY o.OrderID;
-- 6 --
SELECT o.OrderID, o.CustomerID, o.OrderDate
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE c.Country = 'Argentina' OR o.OrderDate < '1996-07-08';
-- 7 --
SELECT ProductID, ProductName, Price
FROM Products
WHERE Price > (SELECT AVG(Price) FROM Products)
ORDER BY Price ASC;
-- 8 --
SELECT DISTINCT o.OrderID, o.CustomerID, o.OrderDate
FROM Orders o
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.Category = 'Dairy Products'
ORDER BY o.OrderID;
-- 9 --
SELECT DISTINCT c.CustomerID, c.CustomerName
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.Category = 'Dairy Products'
ORDER BY c.CustomerID;