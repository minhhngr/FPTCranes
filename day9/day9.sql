CREATE DATABASE Day10;

USE Day10;

CREATE TABLE Employees
(
    EmployeeID INT PRIMARY KEY,
    FirstName  NVARCHAR(50),
    Department NVARCHAR(50),
    Salary     MONEY
);

-- INSERT sample data into Employees table
INSERT INTO Employees
    (EmployeeID, FirstName, Department, Salary)
VALUES
    (1, 'Alice', 'HR', 60000)
    ,(2, 'Bob', 'IT', 75000)
    ,(3, 'Charlie', 'Finance', 80000)
    ,(4, 'David', 'IT', 72000)
    ,(5, 'Eve', 'HR', 65000);

-- Query to select all employees from the IT department
SELECT * FROM Employees;

--CTE: Common Table Expression to find average salary by department

WITH HighSalary AS (SELECT * FROM Employees WHERE Salary > 70000)
SELECT * FROM HighSalary;

--Multiple CTE

WITH SalaryCTE AS 
(
    SELECT *, Salary * 12 AS AnnualSalary FROM Employees
),
RankCTE AS 
(
    SELECT *, RANK() OVER (ORDER BY AnnualSalary DESC) AS SalaryRank FROM SalaryCTE
)
SELECT * FROM RankCTE

