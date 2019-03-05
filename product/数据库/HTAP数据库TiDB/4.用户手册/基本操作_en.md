
### Create, View and Delete Database

Create a database using the CREATE DATABASE statement. Syntax is as follows:

    CREATE DATABASE db_name [options];

For example, to create a database named samp_db, use the following statement:

    CREATE DATABASE IF NOT EXISTS samp_db;

View the database using the SHOW DATABASES statement:

    SHOW DATABASES;

Delete the database using the DROP DATABASE statement. For example:
    
    DROP DATABASE samp_db;

### Create, View and Delete Table

Create a table using the CREATE TABLE statement. Syntax is as follows:

    CREATE TABLE table_name column_name data_type constraint;

For example:

    CREATE TABLE person (
    number INT(11),
    name VARCHAR(255),
    birthday DATE
    );

If the table already exists, add IF NOT EXISTS to prevent an error from occurring:

    CREATE TABLE IF NOT EXISTS person (
      number INT(11),
      name VARCHAR(255),
      birthday DATE
    );

View the table-creating statement using the SHOW CREATE statement. For example:

    SHOW CREATE table person;

View the columns of the table using the SHOW FULL COLUMNS statement. For example:


    SHOW FULL COLUMNS FROM person;

Delete a table using the DROP TABLE statement. For example:


    DROP TABLE person;

Or


    DROP TABLE IF EXISTS person;

View all tables in the database using the SHOW TABLES statement. For example:

    SHOW TABLES FROM samp_db;

### Create, View and Delete Index

For columns whose values are not unique, use the CREATE INDEX or ALTER TABLE statement. For example:

    CREATE INDEX person_num ON person (number);

Or

    ALTER TABLE person ADD INDEX person_num (number);

For columns whose values are unique, you can create a unique index. For example:
    
    CREATE UNIQUE INDEX person_num ON person (number);

Or


    ALTER TABLE person ADD UNIQUE person_num  on (number);

View all indexes in the table using the SHOW INDEX statement:


    SHOW INDEX from person;

Delete an index using the ALTER TABLE or DROP INDEX statement. Similar to the CREATE INDEX statement, DROP INDEX can also be embedded in the ALTER TABLE statement. For example:

    DROP INDEX person_num ON person;
    ALTER TABLE person DROP INDEX person_num;

### Add, Delete, Modify, and Query Data

Insert data into a table using the INSERT statement. For example:


    INSERT INTO person VALUES("1","tom","20170912");

Retrieve the data in table using the SELECT statement to. For example:

    SELECT * FROM person;
    +--------+------+------------+
    | number | name | birthday   |
    +--------+------+------------+
    |  1 | tom  | 2017-09-12 |
    +--------+------+------------+

Modify the data in table using the UPDATE statement. For example:

    UPDATE person SET birthday='20171010' WHERE name='tom';

    SELECT * FROM person;
    +--------+------+------------+
    | number | name | birthday   |
    +--------+------+------------+
    |  1 | tom  | 2017-10-10 |
    +--------+------+------------+

Delete the data in table using the DELETE statement:

    DELETE FROM person WHERE number=1;
    SELECT * FROM person;
    Empty set (0.00 sec)

### Create, Authorize, and Delete users

Create user tiuser with a password of 123456 using the CREATE USER statement:


    CREATE USER 'tiuser'@'localhost' IDENTIFIED BY '123456';

Authorize user tiuser to retrieve tables in database samp_db:


    GRANT SELECT ON samp_db .* TO 'tiuser'@'localhost';

Query user tiuser's permission:


    SHOW GRANTS for tiuser@localhost;

Delete user tiuser:


    DROP USER 'tiuser'@'localhost';

