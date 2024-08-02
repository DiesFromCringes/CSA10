-- lay thong tin khach o Mexico
select * from customers where country = 'mexico'
limit 5;	
-- Country trung nhau
select distinct country from customers;

-- Customers: at Canada, Mexico, USA
select * from customers 
where country in ('canada', 'mexico', 'USA');
-- Ten cong ty: at USA => not SF
select CustomerName from customers 
where country = 'usa' and city != 'San Francisco';
-- ProductName -> name + unit (product): unit=> bottles
select productName as name, unit 
from products
where unit like '%bottles%' or unit like '%bottle%';

-- danh sach san pham => sort theo gia
select * from products
order by price;
-- 5 product (beverages) (price cao nhat)
select * from products
order by price desc
limit 5;

select * from products
where unit like '%boxes%' or unit like '%box%'
and price between 10 and 25;

select * from orders
where OrderDate like '1996-08-__';
select * from orders where OrderDate like '1996-08%';
select * from orders where OrderDate between
'1996-08-01' and '1996-08-31';

select * from orders where OrderDate >=
'1996-08-01' and OrderDate <= '1996-08-31';

-- id + quanity (>10 / order)
select productsID, Quantity from orderdetails
where quantity > 10;