select * from customers;

-- List all customers with their corresponding sales representative's first and last name:
select c.customerName, e.firstName, e.lastName from customers c
	left join employees e
		on c.salesRepEmployeeNumber = e.employeeNumber;

-- Find the product lines with their respective product count:
-- group by
select count(productLine), productLine from products group by productLine order by count(productLine);


-- List all orders along with the customer name and order status:
select o.*, c.customerName  from orders o join customers c
	on c.customerNumber = o.customerNumber;

-- Get the employees who have reported to another employee (i.e., have a manager):
select * from employees;
-- name of employee ,role,  manager name, manager_role
select emp.firstName, emp.jobTitle, managers.firstName as manager_name, managers.jobTitle as manager_role
	from employees emp left join employees managers
		on emp.reportsTo = managers.employeeNumber;

-- create and drop database.
create database test;
drop database test;
drop schema test;


create table persons (
	personId int,
    firstName varchar(255),
    lastname varchar(255),
    address varchar(255),
    city varchar(255)
    );

select * from persons;

use classicmodels1;


-- Create database Lesson3
-- Use that database (use lesson3)
-- Create Table Actors. With columns First name Last name , Age , and Favorite movie
-- insert at least 3 actors with all data.

-- insert into <table_name> (<column1>, <column3>,<column3>... values (<value1>,<value2>,<value3>...);


Create database Lesson3;
use lesson3;
create table actors (
	firstName varchar(255),
    lastname varchar(255),
    age int,
    favorite_movie varchar(255)
    );

select * from actors;
INSERT INTO Actors (firstName, lastname, age, favorite_movie)
VALUES
    ('Tom', 'Hanks', 65, 'Forrest Gump');

INSERT INTO Actors (firstName, lastname, age, favorite_movie)
VALUES
    ('Meryl', 'Streep', 72, 'The Devil Wears Prada'),
    ('Chadwick', 'Boseman', 43, 'Black Panther'),
    ('Emma', 'Watson', 32, 'Harry Potter and the Philosopher''s Stone'),
    ('Chris', 'Hemsworth', 38, 'Thor');

-- To add a column in a table, use the following syntax:
-- ALTER TABLE table_name
-- ADD column_name datatype;
-- Exercise.
-- Add column to the table actors . Column name ‘Gender’ should be varchar(1) -> (m or f)
-- update the table and add genders to all rows
-- update <table_name> set <column_name>= <value> where <some condition>

ALTER TABLE Actors
	ADD gender varchar(1);


select * from Actors;
update Actors set gender = 'm' where firstname in ('tom','Chadwick','Chris');
update Actors set gender = 'f' where gender is null;

alter table Actors drop column gender;

truncate table actors;
drop table actors;


select * from persons2;


insert into persons2 (personid, lastName, firstname) values (2, 'Hanks', 'TOM');


create table persons2 (
	personId int not null,
    firstName varchar(255) not null,
    lastname varchar(255) not null,
    address varchar(255),
    city varchar(255)
    );


CREATE TABLE Persons3 (
ID int PRIMARY KEY,
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Age int);


select * from Persons3;
insert into persons3 (ID, lastName, firstname) values (2, 'Hanks', 'TOM');
insert into persons3 (ID, lastName, firstname) values (3, 'Hanks', 'TOM');
insert into persons3 (ID, lastName, firstname) values (1, 'Julia', 'Roberts');
insert into persons3 (lastName, firstname) values ('Julia', 'Roberts');



create database college;
use college;

CREATE TABLE courses (
  course_id INT NOT NULL ,
  course_name VARCHAR(50) NOT NULL,
  instructor_name VARCHAR(50) NOT NULL,
  course_description TEXT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  PRIMARY KEY (course_id)
);

INSERT INTO courses (course_id ,course_name, instructor_name, course_description, start_date, end_date)
VALUES
(1, 'Intro to Python', 'John Smith', 'Learn the basics of Python programming', '2023-05-01', '2023-06-01'),
(2, 'Web Development', 'Sarah Johnson', 'Learn how to build dynamic websites with HTML, CSS, and JavaScript', '2023-06-15', '2023-08-15'),
(3, 'Data Analysis with R', 'David Lee', 'Analyze and visualize data using the R programming language', '2023-07-01', '2023-08-01');

select * from courses;

CREATE TABLE students (
  student_id INT NOT NULL,
  student_name VARCHAR(50) NOT NULL,
  course_id INT NOT NULL,
  PRIMARY KEY (student_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
);


INSERT INTO students (student_id, student_name, course_id)
VALUES
  (1, 'Jane Doe', 1),  (2, 'John Smith', 2),  (3, 'Sarah Johnson', 3),  (4, 'David Lee', 1),
  (5, 'Emily Brown', 2),  (6, 'Michael Chen', 3),  (7, 'Julia Kim', 1),  (8, 'Alex Wong', 2),
  (9, 'Elena Rodriguez', 3),  (10, 'Chris Patel', 1);

select * from students;



select * from courses;

delete from students where student_id = 1;
delete from students where course_id = 1;
delete from courses where course_id = 1;

delete from courses where course_id = 1	;
drop table students;
drop table courses;

select s.student_name, c.course_description from students s join courses c on s.course_id = c.course_id where c.course_id = 1;

-- Can we insert student without course_id . why?
INSERT INTO students (student_id, student_name) VALUES
  (15, 'Arja Stark');

-- Can we delete course python why?
delete from courses where course_id = 1;

-- How to delete course Python?
update students set course_id = 2 where course_id = 1;
-- 2. delete course python










