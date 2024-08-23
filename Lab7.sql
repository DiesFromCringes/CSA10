SELECT MIN(OrderDate) AS EarliestDate
FROM Orders;
-- 2 --
SELECT COUNT(*) AS TotalOrders
FROM Orders;
-- 3 --
SELECT OrderID, SUM(Quantity) AS TotalItems
FROM OrderDetails
GROUP BY OrderID;
-- 4 --
SELECT AVG(TotalItems) AS AvgItems
FROM (
    SELECT OrderID, SUM(Quantity) AS TotalItems
    FROM OrderDetails
    GROUP BY OrderID
) AS OrderTotals;
-- 5 --
SELECT OrderID, COUNT(DISTINCT ProductID) AS DistinctItems
FROM OrderDetails
GROUP BY OrderID;
-- 6 --
SELECT Category, AVG(Price) AS AvgPrice
FROM Products
GROUP BY Category
HAVING AVG(Price) BETWEEN 20 AND 30;
-- 7 --
SELECT Country, COUNT(*) AS CustomerCount
FROM Customers
GROUP BY Country
HAVING COUNT(*) > 10;
-- 8 --
SELECT CustomerID, COUNT(OrderID) AS Ordered
FROM Orders
GROUP BY CustomerID
ORDER BY Ordered DESC;
-- 9 --
SELECT ProductID, COUNT(DISTINCT OrderID) AS Ordered
FROM OrderDetails
GROUP BY ProductID
HAVING COUNT(DISTINCT OrderID) > 10;
-- 10 --
SELECT ProductID, SUM(Quantity) AS TotalItems
FROM OrderDetails
WHERE ProductID = 1
GROUP BY ProductID;