

-- inner join --
select o.orderId, o.OrderDate, c.CustomerName, C.Address
from orders as o inner join customers as c
on o.CustomerID = c.CustomerID;

-- left join --
select *
from employees as e left join orders as o
on e.EmployeeID = o.EmployeeID;

create table a (
id int auto_increment primary key,
content varchar(100));
create table b (
id int auto_increment primary key,
a_id int, content varchar(100));
insert into a(content) values ('a'), ('b'), ('c');
insert into b(a_id, content) values (1,'a'), (2,'b'), (1,'c');
create table c (id int auto_increment primary key, 
fullname varchar(500), job varchar(50), managed_by int);
insert into c(fullname, job, managed_by) 
values ("Nguyen Van A", "cashier", 3),
		("Nguyen Van B", "CEO", null),
        ("Nguyen Van C", "manager", 2),
        ("Nguyen Van D", "guide", 3);
select *
from b left join a
on a.id = b.a_id;
drop table a; drop table b;

-- self join ---
-- lay thong tin cua quan ly nhan vien 
select table_1.fullname, table_2.fullname as managed_by
from c as table_1 inner join c as table_2
on table_1.managed_by = table_2.id;

select table_1.fullname, table_2.fullname as managed_by
from c as table_1, c as table_2
where table_1.managed_by = table_2.id;