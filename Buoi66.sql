select * from customers;
select city as Customer_City from customers;
select distinct city, country from customers;
select* from customers where customerId = 3;

select * from orders
where orderDate
between '1996-07-01' and '1996-07-05';

select * from products
where productName like '%g%';

select city from customers
where city like '%i%'
group by city;

select * from orderDetails
order by quantiti asc 
