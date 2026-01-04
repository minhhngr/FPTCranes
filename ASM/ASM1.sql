CREATE DATABASE ASM_MinhHuynh_DB;
USE ASM_MinhHuynh_DB;

-- Create table Customers
CREATE TABLE CustomersTb (customer_id   INT PRIMARY KEY
                          , full_name   VARCHAR(100) NOT NULL
                          , email       VARCHAR(100) UNIQUE
                          , phone       VARCHAR(15) UNIQUE
                          , city        VARCHAR(50)
                          , created_at  DATE DEFAULT CURRENT_DATE);

-- Create table Employees
CREATE TABLE EmployeesTb (employee_id  INT PRIMARY KEY
                          , full_name  VARCHAR(100) NOT NULL
                          , position   VARCHAR(50)
                          , salary     DECIMAL(10, 2) CHECK (salary > 0)
                          , hire_date  DATE DEFAULT CURRENT_DATE);

-- Create table Products
CREATE TABLE ProductsTb (product_id     INT PRIMARY KEY
                         , product_name VARCHAR(100)
                         , price        DECIMAL(10, 2) CHECK (price > 0)
                         , stock        INT CHECK (stock >= 0)
                         , category     VARCHAR(50));

-- Create table Orders
CREATE TABLE OrdersTb (order_id       INT PRIMARY KEY
                       , customer_id  INT
                       , employee_id  INT
                       , order_date   DATE DEFAULT CURRENT_DATE
                       , status       VARCHAR(20)
                       , FOREIGN KEY (customer_id) REFERENCES CustomersTb(customer_id)
                       , FOREIGN KEY (employee_id) REFERENCES EmployeesTb(employee_id));

-- Create table OrderDetails
CREATE TABLE OrderDetailsTb (order_id         INT
                             , product_id     INT
                             , quantity       INT
                             , unit_price     DECIMAL(10, 2)
                             , PRIMARY KEY (order_id, product_id)
                             , FOREIGN KEY (order_id)   REFERENCES OrdersTb(order_id)
                             , FOREIGN KEY (product_id) REFERENCES ProductsTb(product_id));

-- Insert data into CustomersTb
INSERT INTO CustomersTb
VALUES 
    (1,'Nguyen Van A','a@gmail.com','090000001','Hanoi','2023-01-01'),
    (2,'Tran Van B','b@gmail.com','090000002','Hanoi','2023-01-02'),
    (3,'Le Van C','c@gmail.com','090000003','HCM','2023-01-03'),
    (4,'Pham Van D','d@gmail.com','090000004','Danang','2023-01-04'),
    (5,'Hoang Van E','e@gmail.com','090000005','Hanoi','2023-01-05'),
    (6,'Nguyen Van F','f@gmail.com','090000006','HCM','2023-01-06'),
    (7,'Tran Van G','g@gmail.com','090000007','Danang','2023-01-07'),
    (8,'Le Van H','h@gmail.com','090000008','Hanoi','2023-01-08'),
    (9,'Pham Van I','i@gmail.com','090000009','HCM','2023-01-09'),
    (10,'Hoang Van J','j@gmail.com','090000010','Hanoi','2023-01-10'),
    (11,'User 11','u11@gmail.com','090000011','HCM','2023-01-11'),
    (12,'User 12','u12@gmail.com','090000012','Danang','2023-01-12'),
    (13,'User 13','u13@gmail.com','090000013','Hanoi','2023-01-13'),
    (14,'User 14','u14@gmail.com','090000014','HCM','2023-01-14'),
    (15,'User 15','u15@gmail.com','090000015','Danang','2023-01-15'),
    (16,'User 16','u16@gmail.com','090000016','Hanoi','2023-01-16'),
    (17,'User 17','u17@gmail.com','090000017','HCM','2023-01-17'),
    (18,'User 18','u18@gmail.com','090000018','Danang','2023-01-18'),
    (19,'User 19','u19@gmail.com','090000019','Hanoi','2023-01-19'),
    (20,'User 20','u20@gmail.com','090000020','HCM','2023-01-20');

SELECT * FROM CustomersTb;

-- Insert data into EmployeesTb
INSERT INTO EmployeesTb
VALUES
    (1,'Employee 1','Sales',800,'2022-01-01'),
    (2,'Employee 2','Sales',850,'2022-02-01'),
    (3,'Employee 3','Sales',900,'2022-03-01'),
    (4,'Employee 4','Sales',950,'2022-04-01'),
    (5,'Employee 5','Manager',1200,'2021-01-01'),
    (6,'Employee 6','Sales',880,'2022-05-01'),
    (7,'Employee 7','Sales',870,'2022-06-01'),
    (8,'Employee 8','Sales',860,'2022-07-01'),
    (9,'Employee 9','Sales',890,'2022-08-01'),
    (10,'Employee 10','Sales',910,'2022-09-01'),
    (11,'Employee 11','Sales',920,'2022-10-01'),
    (12,'Employee 12','Sales',930,'2022-11-01'),
    (13,'Employee 13','Sales',940,'2022-12-01'),
    (14,'Employee 14','Sales',950,'2023-01-01'),
    (15,'Employee 15','Sales',960,'2023-02-01'),
    (16,'Employee 16','Sales',970,'2023-03-01'),
    (17,'Employee 17','Sales',980,'2023-04-01'),
    (18,'Employee 18','Sales',990,'2023-05-01'),
    (19,'Employee 19','Sales',1000,'2023-06-01'),
    (20,'Employee 20','Manager',1300,'2020-01-01');

SELECT * FROM EmployeesTb;

-- Insert data into ProductsTb
INSERT INTO ProductsTb
VALUES
    (1,'Laptop Dell',1500,50,'Electronics'),
    (2,'Laptop HP',1400,40,'Electronics'),
    (3,'Laptop Asus',1300,60,'Electronics'),
    (4,'iPhone 14',1200,30,'Phone'),
    (5,'Samsung S23',1100,35,'Phone'),
    (6,'Xiaomi 13',900,45,'Phone'),
    (7,'iPad Air',800,25,'Tablet'),
    (8,'iPad Pro',1000,20,'Tablet'),
    (9,'AirPods',200,100,'Accessory'),
    (10,'Headphone Sony',300,80,'Accessory'),
    (11,'Mouse Logitech',50,200,'Accessory'),
    (12,'Keyboard Corsair',150,150,'Accessory'),
    (13,'Monitor LG',400,70,'Electronics'),
    (14,'Monitor Samsung',420,65,'Electronics'),
    (15,'Printer HP',350,40,'Office'),
    (16,'Scanner Canon',330,30,'Office'),
    (17,'Webcam Logitech',120,90,'Accessory'),
    (18,'SSD Samsung 1TB',180,110,'Storage'),
    (19,'HDD WD 2TB',160,100,'Storage'),
    (20,'USB Kingston 64GB',30,300,'Storage');

SELECT * FROM ProductsTb;

-- Insert data into OrdersTb
INSERT INTO OrdersTb
VALUES
    (1,1,1,'2023-02-01','Completed'),
    (2,2,2,'2023-02-02','Completed'),
    (3,3,3,'2023-02-03','Completed'),
    (4,4,4,'2023-02-04','Completed'),
    (5,5,5,'2023-02-05','Completed'),
    (6,6,6,'2023-02-06','Completed'),
    (7,7,7,'2023-02-07','Completed'),
    (8,8,8,'2023-02-08','Completed'),
    (9,9,9,'2023-02-09','Completed'),
    (10,10,10,'2023-02-10','Completed'),
    (11,11,11,'2023-03-01','Completed'),
    (12,12,12,'2023-03-02','Completed'),
    (13,13,13,'2023-03-03','Completed'),
    (14,14,14,'2023-03-04','Completed'),
    (15,15,15,'2023-03-05','Completed'),
    (16,16,16,'2023-03-06','Completed'),
    (17,17,17,'2023-03-07','Completed'),
    (18,18,18,'2023-03-08','Completed'),
    (19,19,19,'2023-03-09','Completed'),
    (20,20,20,'2023-03-10','Completed');

SELECT * FROM OrdersTb;

-- Insert data OrderDetailsTb
INSERT INTO OrderDetailsTb
VALUES
    (1,1,1,1500),
    (1,9,2,200),
    (2,2,1,1400),
    (2,11,3,50),
    (3,3,1,1300),
    (3,12,1,150),
    (4,4,2,1200),
    (4,9,1,200),
    (5,5,1,1100),
    (5,10,1,300),
    (6,6,2,900),
    (6,11,2,50),
    (7,7,1,800),
    (7,9,2,200),
    (8,8,1,1000),
    (8,12,1,150),
    (9,13,2,400),
    (9,11,2,50),
    (10,14,1,420),
    (10,9,3,200),
    (11,15,1,350),
    (11,20,5,30),
    (12,16,1,330),
    (12,18,1,180),
    (13,17,2,120),
    (13,11,2,50),
    (14,18,1,180),
    (14,19,1,160),
    (15,1,1,1500),
    (15,20,10,30),
    (16,2,1,1400),
    (16,11,3,50),
    (17,3,1,1300),
    (17,12,1,150),
    (18,4,1,1200),
    (18,9,2,200),
    (19,5,1,1100),
    (19,10,1,300),
    (20,6,1,900),
    (20,11,4,50);

SELECT * FROM OrderDetailsTb;

----------
----------
----------
-- Queries
----------
----------


-- 1. List customer have never place any order.
--
INSERT INTO CustomersTb
VALUES
    (21,'No Order A','noa@gmail.com','090000021','Hanoi','2023-02-01'),
    (22,'No Order B','nob@gmail.com','090000022','HCM','2023-02-02'),
    (23,'No Order C','noc@gmail.com','090000023','Danang','2023-02-03');

--
SELECT * 
FROM CustomersTb 
WHERE customer_id 
 NOT IN (SELECT DISTINCT customer_id 
         FROM OrdersTb);



-- 2. Total amount of each order
--
SELECT o.order_id
       , SUM(od.quantity * od.unit_price) AS total_amount
FROM OrdersTb o
JOIN OrderDetailsTb od 
 ON o.order_id = od.order_id
GROUP BY o.order_id;



-- 3. Employees highest number of orders
--
INSERT INTO OrdersTb 
VALUES
    (21,1,1,'2023-04-01','Completed'),
    (22,2,1,'2023-04-02','Completed'),
    (23,3,1,'2023-04-03','Completed');

--
SELECT employee_id, total_orders
FROM (SELECT employee_id
             , COUNT(order_id) AS total_orders
      FROM OrdersTb
      GROUP BY employee_id) AS emp_orders
WHERE total_orders = (SELECT MAX(total_orders)
                      FROM (SELECT COUNT(employee_id) AS total_orders
                            FROM OrdersTb
                            GROUP BY employee_id) AS max_orders);



-- 4. Top 3 best-selling products
--
INSERT INTO OrderDetailsTb 
VALUES
    (21,1,5,1500),
    (22,1,5,1500),
    (23,9,10,200);

--
WITH ProductSales AS (
    SELECT p.product_id
           , p.product_name
           , SUM(od.quantity) AS total_sold
           , RANK() OVER (ORDER BY SUM(od.quantity) DESC) AS rnk
    FROM ProductsTb p
    JOIN OrderDetailsTb od 
     ON p.product_id = od.product_id
    GROUP BY p.product_id, p.product_name
)
SELECT product_id, product_name, total_sold
FROM ProductSales
WHERE rnk <= 3;


-- 5. Total Revenue each month
--
INSERT INTO OrdersTb 
VALUES
    (29,4,2,'2023-01-15','Completed'),
    (30,5,3,'2023-04-10','Completed');

INSERT INTO OrderDetailsTb 
VALUES
    (29,2,1,1400),
    (30,3,2,1300);

--
SELECT YEAR(o.order_date) AS order_year
       , MONTH(o.order_date) AS order_month
       , SUM(od.quantity * od.unit_price) AS total_revenue
FROM OrdersTb o
JOIN OrderDetailsTb od 
 ON o.order_id = od.order_id
GROUP BY YEAR(o.order_date), MONTH(o.order_date)
ORDER BY order_year, order_month;



-- 6. Customer highest total
--
WITH CustomerHighest AS (
    SELECT c.customer_id
           , c.full_name
           , SUM(od.quantity * od.unit_price) AS total_spent
           , RANK() OVER (ORDER BY SUM(od.quantity * od.unit_price) DESC) AS rnk
    FROM CustomersTb c
    JOIN OrdersTb o
     ON c.customer_id = o.customer_id
    JOIN OrderDetailsTb od
     ON o.order_id = od.order_id
    GROUP BY c.customer_id, c.full_name
)
SELECT customer_id, full_name, total_spent
FROM CustomerHighest
WHERE rnk = 1;


-- 7. List Products never sold
INSERT INTO ProductsTb 
VALUES
    (21,'Not Sold A',500,50,'Test'),
    (22,'Not Sold B',600,60,'Test'),
    (23,'Not Sold C',700,70,'Test');

--
SELECT *
FROM ProductsTb p
WHERE p.product_id 
 NOT IN (SELECT DISTINCT od.product_id 
         FROM OrderDetailsTb od);



-- 8. Total revenue highest city
INSERT INTO OrdersTb 
VALUES
    (27,3,5,'2023-03-25','Completed');

--
SELECT TOP 1 WITH TIES c.city
                       , SUM(od.quantity * od.unit_price) AS total_revenue
FROM CustomersTb c
JOIN OrdersTb o
 ON c.customer_id = o.customer_id
JOIN OrderDetailsTb od
 ON o.order_id = od.order_id
GROUP BY c.city
ORDER BY total_revenue DESC;



-- 9. Total quantity product >= 10
--
SELECT p.product_id
       , p.product_name
       , SUM(od.quantity) AS total_qty_product
FROM ProductsTb p
JOIN OrderDetailsTb od 
 ON p.product_id = od.product_id
GROUP BY p.product_id, p.product_name
HAVING SUM(od.quantity) >= 10
ORDER BY total_qty_product DESC;



-- 10. Employees has total revenue higher than avg revenue
--
SELECT e.employee_id
       , e.full_name
       , SUM(od.quantity * od.unit_price) AS total_revenue
FROM EmployeesTb e
JOIN OrdersTb o
 ON e.employee_id = o.employee_id
JOIN OrderDetailsTb od
 ON o.order_id = od.order_id
GROUP BY e.employee_id, e.full_name
HAVING SUM(od.quantity * od.unit_price) > (SELECT AVG(total_rev) 
                                           FROM (SELECT SUM(od2.quantity * od2.unit_price) AS total_rev
                                                 FROM EmployeesTb e2
                                                 JOIN OrdersTb o2
                                                  ON e2.employee_id = o2.employee_id
                                                 JOIN OrderDetailsTb od2
                                                  ON o2.order_id = od2.order_id
                                                 GROUP BY e2.employee_id) AS avg_rev);