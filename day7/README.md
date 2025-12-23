# Day 7

## Database

- Common Database Systems
  - MySQL
  - PostgreSQL
  - SQLite
  - MongoDB
  - Redis
- NoSQL

Key Characteristics
    - Schema-less
    - Scalability
    - Flexibility
    - Security
    - Organization Structures
    - Efficiency
    - Data Integration
    - Multi-User Support

What is a relational database?
A relational database is a type of database that stores and provides access to data points that are related to one another. Data in a relational database is organized into tables (also known as relations) consisting of rows and columns. Each table represents a specific entity, and each row in the table represents a unique record, while each column represents a field or attribute of that record.

- Key Principles of Relational Databases
  - Tables (Relations): Data is organized into tables.
  - Rows (Tuples): Each row represents a single record in a table.
  - Columns (Attributes): Each column represents a field or attribute of the record.
  - Primary Keys: Unique identifiers for records in a table.
  - Foreign Keys: Fields that create a link between tables.
  - Relationships: Associations between tables.
  - Normalization: Process of organizing data to reduce redundancy.
  - Relationships between Tables
    - One-to-One
    - One-to-Many
    - Many-to-Many
- Advantages of Relational Databases
  - Data Integrity: Ensures accuracy and consistency of data.
  - ACID Compliance: Guarantees reliable transactions.
  - Flexibility: Allows complex queries and data manipulation.
  - Scalability: Can handle large amounts of data and users.
  - Security: Protects data from unauthorized access.
  - Ease of Use: User-friendly interfaces and query languages.
  - Reduced data redundancy through normalization.
  - Powerful querying capabilities using SQL.
- Disadvantages of Relational Databases
  - Complexity: Can be complex to design and manage.
  - Performance: May not perform well with very large datasets or high transaction volumes.
  - Scalability: Can be challenging to scale horizontally.
  - Cost: Licensing and maintenance can be expensive.
  - Rigid Schema: Changes to the schema can be difficult and time-consuming.
  - Limited support for unstructured data.
- Use Cases of Relational Databases
  - E-commerce platforms
  - Banking and financial systems
  - Customer relationship management (CRM) systems
  - Enterprise resource planning (ERP) systems
  - Healthcare management systems
  - Inventory management systems
  - Content management systems (CMS)
- Popular Relational Database Management Systems (RDBMS)
  - MySQL
  - PostgreSQL
  - Oracle Database
  - Microsoft SQL Server
  - SQLite
- SQL (Structured Query Language)
  - Data Definition Language (DDL)
    - CREATE
    - ALTER
    - DROP
  - Data Manipulation Language (DML)
    - SELECT
    - INSERT
    - UPDATE
    - DELETE
  - Data Control Language (DCL)
    - GRANT
    - REVOKE
  - Transaction Control Language (TCL)
    - COMMIT
    - ROLLBACK
    - SAVEPOINT
- Basic SQL Commands
  - SELECT: Retrieve data from a database.
  - INSERT: Add new data to a database.
  - UPDATE: Modify existing data in a database.
  - DELETE: Remove data from a database.
  - CREATE TABLE: Create a new table in the database.
  - ALTER TABLE: Modify an existing table structure.
  - DROP TABLE: Delete a table from the database.
- Joins in SQL
  - INNER JOIN: Returns records that have matching values in both tables.
  - LEFT JOIN (or LEFT OUTER JOIN): Returns all records from the left table and the matched records from the right table.
  - RIGHT JOIN (or RIGHT OUTER JOIN): Returns all records from the right table and the matched records from the left table.
  - FULL JOIN (or FULL OUTER JOIN): Returns all records when there is a match in either left or right table.
- Indexing
  - Improves query performance by reducing the amount of data that needs to be scanned.
  - Types of Indexes
    - Single-column Indexes
    - Composite Indexes
    - Unique Indexes
    - Full-text Indexes
- Backup and Recovery
  - Regular backups to prevent data loss.
  - Recovery strategies to restore data in case of failure.
- Database Security
  - User authentication and authorization.
  - Data encryption.
  - Regular security audits.
- Database Design Best Practices
  - Normalize data to reduce redundancy.
  - Use meaningful table and column names.
  - Implement proper indexing strategies.
  - Regularly back up the database.
  - Monitor performance and optimize queries.
  - Ensure data integrity through constraints.
- Future Trends in Databases
  - Cloud Databases
  - NoSQL Databases
  - NewSQL Databases
  - Database as a Service (DBaaS)
  - Artificial Intelligence and Machine Learning Integration
  - Edge Computing Databases
  - Blockchain Databases

Database Basic

- What is a table
A table is a collection of related data organized in rows and columns within a database. Each table represents a specific entity, such as customers, products, or orders, and is used to store and manage data efficiently. Tables are fundamental components of relational databases, allowing for structured data storage and retrieval.=

- What is a record
A record, also known as a row or tuple, is a single entry in a database table that contains related data fields. Each record represents a unique instance of the entity defined by the table, with each field (or column) in the record holding a specific piece of information about that instance.

- What is a rows
In a database table, a row (also known as a record or tuple) represents a single, complete set of related data fields for a specific entity. Each row contains values for each column in the table, corresponding to the attributes defined for that entity. For example, in a "Customers" table, each row would represent an individual customer with their respective details such as name, address, and contact information.

- What are Data Types?

Common Data Types in Databases:
    - Integer: Whole numbers (e.g., 1, 2, 3).
    - Float/Double: Decimal numbers (e.g., 3.14, 2.718).
    - Char: Fixed-length character strings (e.g., 'A', 'Hello').
    - Varchar: Variable-length character strings (e.g., 'Hello World').
    - Text: Large text data (e.g., articles, descriptions).
    - Date: Date values (e.g., '2023-01-01').
    - Time: Time values (e.g., '12:30:00').
    - Boolean: True/False values.
    - Blob: Binary large objects for storing binary data (e.g., images, files).

Example Table with DAata Types:

CREATE TABLE Employees (
    ID Integer PRIMARY KEY,
    Name Varchar(100),
    Age Integer,
    JoinDate Date,
    IsActive Boolean
);

| ID (Integer) | Name (Varchar) | Age (Integer) | JoinDate (Date) | IsActive (Boolean) |
|--------------|----------------|---------------|---------------------|----------------|
| 1            | John Doe       | 30            | 2022-01-15        | True             |
| 2            | Jane Smith     | 25            | 2023-03-22        | False            |

Understanding the Relational Database Model

The relational database model is a way of organizing data into tables (also called relations) that consist of rows and columns. Each table represents a specific entity, and each row in the table represents a unique record, while each column represents a field or attribute of that record. The relational model is based on the principles of set theory and predicate logic, allowing for efficient data storage, retrieval, and manipulation.

Common Components of the Relational Database Model:

- Tables (Relations): Data is organized into tables.
- Rows (Tuples): Each row represents a single record in a table.
- Columns (Attributes): Each column represents a field or attribute of the record.
- Primary Keys: Unique identifiers for records in a table.
- Foreign Keys: Fields that create a link between tables.
- Relationships: Associations between tables.
- Normalization: Process of organizing data to reduce redundancy.

Three Types of Table Relationships:

1. One-to-One (1-1): Each record in Table A is linked to one and only one record in Table B, and vice versa.

    Example: Person <==> Passport

    - Each person has one unique passport, and each passport is assigned to one person.
2. One-to-Many (1-N): A record in Table A can be linked to multiple records in Table B, but each record in Table B is linked to only one record in Table A.

    Example: Customer <==> Orders

    - One customer can place multiple orders, but each order is associated with only one customer.

3. Many-to-Many (N-N): Records in Table A can be linked to multiple records in Table B, and vice versa. This relationship often requires a junction table to manage the associations.

    Example: Students <==> Courses
    - One student can enroll in multiple courses, and each course can have multiple students enrolled.
    - One course can have multiple students enrolled, and one student can enroll in multiple courses.
    Requires a junction table (e.g., Enrollments) to manage the associations.

Requires a junction table (e.g., Enrollments) to manage the associations.

students table:

| StudentID | StudentName |
|-----------|-------------|
| 1         | Alice       |
| 2         | Bob         |

courses table:

| CourseID | CourseName  |
|----------|-------------|
| 101      | Math        |
| 102      | Science     |

enrollments table:

| EnrollmentID | StudentID | CourseID  |
|-----------   |-----------|-----------|
| 1            | 1         | 101       | Alice is enrolled in Math
| 2            | 1         | 102       | Alice is enrolled in Science
| 3            | 2         | 101       | Bob is enrolled in Math

The junction table (enrollments) connects students and courses, allowing for the many-to-many relationship between them. (foreign keys: StudentID references students table, CourseID references courses table)

## Primary Key

A primary key is a unique identifier for each record in a database table. It ensures that each record can be uniquely identified and accessed. A primary key must contain unique values and cannot contain NULL values. It is typically defined on one or more columns of a table.

Primary Key Rules:

- MUST contain unique values.
- CANNOT contain NULL values.
- Each table can have only ONE primary key.

Example of Defining a Primary Key in SQL:

```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    HireDate DATE
);

EmployeeID is the primary key for the Employees table, ensuring that each employee record is uniquely identifiable.
```

## Foreign Key

A foreign key is a field (or a set of fields) in one table that uniquely identifies a row of another table. The purpose of the foreign key is to ensure referential integrity of the data. In other words, it establishes a link between the data in two tables.

Foreign Key Rules:

- Refers to the primary key in another table.
- Can contain duplicate values.
- Can contain NULL values.
- Can have duplicate foreign keys in the child table.
- Maintains referential integrity between the two tables.
- A table can have multiple foreign keys.

Example: Order and Customers

```sql
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    OrderDate DATE,
    CustomerID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
```

Customers Table:

| CustomerID | CustomerName    |
|------------|-----------------|
| 1          | John Doe        |
| 2          | Jane Smith      |

Orders Table:

| OrderID | OrderDate  | CustomerID |
|---------|------------|------------|
| 101     | 2023-01-15 | 1          | <-- Order placed by John Doe
| 102     | 2023-01-16 | 2          | <-- Order placed by Jane Smith
| 103     | 2023-01-17 | 1          | <-- Another order placed by John Doe

## Constraints Definition

Constraints are rules enforced on data columns in a database table to ensure the integrity, accuracy, and reliability of the data. They help maintain the quality of the data by restricting the types of data that can be inserted into a table.

Types of Constraints:

- NOT NULL: Ensures that a column cannot have a NULL value.
- UNIQUE: Ensures that all values in a column are unique.
- PRIMARY KEY: A combination of NOT NULL and UNIQUE. Uniquely identifies each record in a table.
- FOREIGN KEY: Ensures referential integrity by linking two tables together.
- CHECK: Ensures that all values in a column satisfy a specific condition.
- DEFAULT: Sets a default value for a column when no value is specified.

## SQL?

SQL (Structured Query Language) is a standardized programming language used for managing and manipulating relational databases. It is used to perform various operations on the data stored in a database, such as querying, updating, inserting, and deleting records. SQL provides a way to interact with the database using simple and intuitive commands.

5 Types of SQL Commands:

- Data Definition Language (DDL)
  - Purpose: Used to define and manage database structures such as tables, indexes, and schemas.
  - Key COmmands:
    - CREATE: Create new database objects (e.g., tables, indexes).
    - ALTER: Modify existing database objects.
    - DROP: Delete database objects.
    - TRUNCATE: Remove all records from a table without logging individual row deletions.
    - RENAME: Change the name of a database object.
  - Notes: Rollback is not possible after executing DDL commands as they are auto-committed.

- Data Manipulation Language (DML)
  - Purpose: Used to manipulate and manage data within database tables.
  - Key Commands:
    - INSERT: Add new records to a table.
    - UPDATE: Modify existing records in a table.
    - DELETE: Remove records from a table.
    - MERGE: Combine data from two tables based on a specified condition.
  - Notes: Affects table rows, and changes can be rolled back if within a transaction.

- Data Control Language (DCL)
  - Purpose: Used to control access to data within the database.
  - Key Commands:
    - GRANT: Give users access privileges to database objects.
    - REVOKE: Remove users' access privileges to database objects.
  - Notes: Primarily focuses on permissions and security.

- Transaction Control Language (TCL)
  - Purpose: Used to manage transactions within the database.
  - Key Commands:
    - COMMIT: Save all changes made during the current transaction.
    - ROLLBACK: Undo changes made during the current transaction.
    - SAVEPOINT: Set a point within a transaction to which you can later roll back.
  - Notes: Ensures data integrity and consistency during transactions.

- Data Query Language (DQL)
  - Purpose: Used to manage transactions within the database.
  - Key Commands:
    - SELECT: Retrieve data from the database.
    - COMMIT: Save all changes made during the current transaction.
    - ROLLBACK: Undo changes made during the current transaction.
    - SAVEPOINT: Set a point within a transaction to which you can later roll back.
  - Notes: Ensures data integrity and consistency during transactions.
