-- sever => database => schema => table => prop --

CREATE DATABASE school;
use school;

alter database school
READ ONLY = 0;

create table students (
	id varchar(12) PRIMARY KEY,
	email varchar(255) unique not null,
    firstname varchar(255) not null
);
alter table students
add column lastname varchar(100);

alter table students
modify lastname varchar(100)
after firstname;

alter table students
rename column id to students_id;

select *
from students;

create table classes (
	class_id varchar(12) primary key,
    title varchar(1000),
    description varchar(5000)
);
select * from classes;

--
create table enrollments (
	students_id varchar(12) not null,
	class_id varchar(12) not null,
    constraint foreign key (students_id)
    references students(students_id),
    constraint foreign key (class_id)
    references classes(class_id)
);

select * from enrollments;

drop table classes;
drop table enrollments;

create table enrollments(
	enrollment_id varchar(12) primary key,
    students_id varchar(12) not null,
    class_id varchar(12) not null
);

alter table enrollments
add constraint foreign key (students_id)
references students(students_id);

alter table enrollments
add constraint foreign key (class_id)
references class(class_id);

insert into students(students_id, firstname, lastname)
values ('000111', 'Nguyen', 'Van Hello');
update students 
set email = 'hello@gmail.com'
where students_id = '000111'

insert into students
values ('000110', 'hi@gmail.com', 'Nguyen', 'Van Hi');

select * from students;
