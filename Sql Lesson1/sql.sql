-- select * from customers;
-- get the order date from the orders table

select * from orders;
select  status,orderDate from orders;

select * from customers where country = 'usa' ;


select * from products order by buyPrice desc;

select * from products order by productName;

select *  from customers order by country asc, customerName desc;


INSERT INTO Customers (CustomerName, ContactLastName, Addressline1, City, PostalCode, Country)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');


select * from customers where CustomerName = 'Cardinal';
update customers set contactLastName = 'Stark', contactFirstname = 'Arja' , city = 'Winterfell' where customerNumber = 497      ;

delete from customers where customerNumber = 497;
