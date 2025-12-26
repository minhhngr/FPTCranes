CREATE DATABASE DAY2

USE DAY2

CREATE TABLE Customer_tb
(
    cusId int primary key,
    cusName nvarchar(150),
    dob date,
    phone char(15),
    email varchar(50) unique
)

--them 5 du lieu vao bang (seed data)
INSERT INTO Customer_tb
values
    (1, N'Nguyễn Văn A', '2000-01-01', '123456789', 'a@gmail'),
    (2, N'Nguyễn Văn B', '1999-01-01', '123456789', 'b@gmail'),
    (3, N'Nguyễn Văn C', '2000-01-01', '123456789', 'c@gmail'),
    (4, N'Nguyễn Văn D', '2000-01-01', '123456789', 'd@gmail'),
    (5, N'Nguyễn Văn E', '2000-01-01', '123456789', 'e@gmail')

SELECT *
FROM Customer_tb

--DROP TABLE Customer_tb

set dateformat dmy

INSERT INTO Customer_tb
values
    (6, N'Nguyễn Văn C1', '26-12-1999', '123456789', 'c1@gmail')

SELECT *
FROM Customer_tb
WHERE email IN ('a@gmail', 'b@gmail', 'c@gmail')

SELECT *
FROM Customer_tb
WHERE cusId BETWEEN 3 and 5

CREATE TABLE Order_tb
(
    orId int primary key identity(1,1),
    cusId int,
    proName varchar(50),
    orDate datetime default GETDATE(),
    constraint FK_Order_Customer foreign key (cusId)
 references Customer_tb(cusId)
)

--seed data for Order_tb (3 records)
INSERT INTO Order_tb
    (cusId, proName)
values
    (1, 'Iphone 13'),
    (2, 'Iphone 17'),
    (6, 'Iphone 14')

SELECT *
FROM Order_tb


--JOIN TABLE
SELECT orId,
    o.cusId,
    email
FROM Order_tb o
    JOIN Customer_tb c ON o.cusId = c.cusId


SELECT orId,
    o.cusId,
    cusName,
    email
FROM Customer_tb c --left
    LEFT JOIN Order_tb o ON o.cusId = c.cusId

--sua bang (them/xoa/sua cot)
ALTER TABLE Order_tb
ADD price int

INSERT INTO Order_tb
    (price)
values
    (1000),
    (2000),
    (1500)

select *
from Order_tb

DELETE FROM Order_tb WHERE orId BETWEEN 6 and 8

UPDATE Order_tb SET price = 1000 WHERE orId = 1
UPDATE Order_tb SET price = 2000 WHERE orId = 2
UPDATE Order_tb SET price = 1500 WHERE orId = 3

SELECT COUNT(CusId)
FROM Order_tb

SELECT SUM(price) as Total_Price
FROM Order_tb

SELECT MAX(orId)
FROM Order_tb

INSERT INTO Order_tb
    (cusId, proName, price)
VALUES
    (3, 'Iphone 15', 2500),
    (4, 'Iphone 16', 3000),
    (5, 'Iphone 18', 3500)

-- asc
SELECT *
FROM Order_tb
ORDER BY price DESC, orId ASC, cusId DESC

SELECT cusID
FROM Customer_tb
GROUP BY cusID

SELECT *
FROM Order_tb

INSERT INTO Order_tb
    (cusId, proName, price)
VALUES
    (1, 'Iphone 13', 1200),
    (1, 'Iphone 14', 1300),
    (2, 'Iphone 17', 2200),
    (2, 'Iphone 18', 2300),
    (3, 'Iphone 15', 2600),
    (3, 'Iphone 16', 2700)

SELECT cusID
    , COUNT(cusId) AS "so_lan_mua_hang"
    , MAX(price) AS "gia_max"
    , proName
FROM Order_tb
GROUP BY cusID, proName
HAVING MAX(price) > 500

SELECT TOP 2
    *
FROM Order_tb
ORDER BY price DESC

--in ten nguoi mua hang nhieu nhat (k xai join)
SELECT cusName
FROM Customer_tb
WHERE cusId = (SELECT cusId FROM Order_tb
                GROUP BY cusID
                ORDER BY COUNT(cusId) DESC)

SELECT cusID FROM Order_tb
GROUP BY cusID
HAVING COUNT(cusId) = (
    SELECT MAX(order_count) FROM (
        SELECT COUNT(cusId) AS order_count
        FROM Order_tb
        GROUP BY cusID
    ) AS counts
)


SELECT o.cusID, c.cusName
FROM Order_tb o
JOIN Customer_tb c ON o.cusId = c.cusId
GROUP BY o.cusID, c.cusName
HAVING COUNT(o.cusId) = (
    SELECT MAX(order_count) FROM (
        SELECT COUNT(cusId) AS order_count
        FROM Order_tb
        GROUP BY cusID
    ) AS counts
)
ORDER BY COUNT(o.cusId) DESC

SELECT TOP 1 WITH TIES o.cusId, COUNT(o.cusId)
FROM Customer_tb c
JOIN Order_tb o ON o.cusId = c.cusId
GROUP BY o.cusID
ORDER BY COUNT(O.cusId) DESC


-- SELECT TOP 1 cusId
-- FROM Order_tb
-- GROUP BY cusID
-- ORDER BY COUNT(cusId) DESC

