select * from Customers where country = 'Australia';

select * from customers where country = 'Germany';

select * from customers order by country , customerName desc; 

-- update the ContactName to "Juan" for all records where country is "Spain":
update customers set contactFirstName = 'Juan' where country = 'Spain';


select * from customers where country = 'spain';

-- insert into the table payments new record with the following values : customerNumber = 112, checkNumber= 'BR23232' , amount = 1000
-- select * from payments;
insert into payments  (customerNumber, checkNumber, amount) values(112, 'BR23232' , 1000);

select * from payments where customerNumber = 112;

-- DELETE FROM table_name WHERE condition;
delete from payments  where customerNumber = 112;


-- get productName and price from products table reduced by 5
select * from products;
select productName, buyPrice-5 from products;

select * from products where productLine != 'Motorcycles';

select * from products where productLine not like 'c%car%';


SELECT * FROM products where productLine in ('classic cars', 'motorcycles') and id between 11 and 35;


-- Find all employees whose last names do not start with 'S'.
select * from employees where lastName not like 'j%';

-- Retrieve all products priced between $10 and $50, and whose names contain the word "dodge".
select * from products where buyprice between 10 and 50 and productName like '%dodge%';

-- Get all customers who have a credit limit greater than $50000 and are located in either 'USA' or 'Canada'.
select * from customers where creditLimit > 50000 and (country = 'USA' or country = 'Canada');

-- Retrieve all offices located in the 'United States' with a 'phone' number starting with the area code '212'.
select * from offices where country = 'USA' and phone like '%212%';

-- Get all order details for products with a price greater than $100.
select * from orderDetails where priceEach > 100;


-- select minimum price from products.
select buyPrice as my_price , productName as my_name, products.* from products;


update products set buyPrice = null where id = 3;

select count(*) from products where buyPrice > 20;

select * from orderDetails where productCode = 's18_2795';

select sum(quantityOrdered * priceEach) as total_sum from  orderDetails where productCode = 's18_2795';

select * from orders where orderDate = '2003-01-09';

select * from customers where state is not null;


SELECT sum(creditLimit), Country
FROM Customers
GROUP BY Country
order by sum(creditLimit) desc;


select * from customers;
select * from orders;
select * from offices;

-- display customers, city , office code which match to the customer.
select customers.contactFirstName, customers.contactLastName, customers.city, offices.officeCode  
	from customers 
		inner join offices on offices.city = customers.city;
        
select c.contactFirstName, c.contactLastName, c.city, o.officeCode  
	from customers c
		join offices o on o.city = c.city;      
        
        
select c.contactFirstName, c.contactLastName, o.city, o.officeCode  
	from offices o
		left join  customers c on o.city = c.city;      
        
-- get order number customer number and customer first name for all customers which have orders        
select o.orderNumber, o.customerNumber, c.contactFirstName, c.* from orders o join customers c on o.customerNumber = c.customerNumber;


SELECT Customers.CustomerName, Orders.orderNumber
FROM Customers
LEFT JOIN Orders ON Customers.customerNumber = Orders.customerNumber
ORDER BY Customers.CustomerName;

select min(creditLimit), city
from customers
group by city;















