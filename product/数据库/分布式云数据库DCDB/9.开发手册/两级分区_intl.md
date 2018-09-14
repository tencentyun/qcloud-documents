
> If you need to view or download the full development documents, please see [Development Guide for DCDB](https://cloud.tencent.com/document/product/557/7714).

#### Two-level partition
DCDB only supports splitting data by HASH, which is not suitable for data under specific conditions, such as log type and old data deletion. To address this problem, two-level partitioning can be used.
DCDB supports two-level partition in range and list formats. The specific syntax for table creation is similar to the MySQL partition syntax.

>Note: The partition uses the less-than sign (<), so if you want to store the data of the year of 2017, you need to create a partition of `<2018`. You only need to create the partition to the current time, and DCDB will automatically add the subsequent partitions. By default, three partitions are created. Taking YEAR as an example, DCDB will automatically create partitions of 2018, 2019, and 2020. Subsequent changes will be automatically made.

Supported range types

- DATE, DATETIME, and TIMESTAMP
		Support functions of year, month, and day. If the function is empty, it adopts the day function.

- TINYINT, SMALLINT, MEDIUMINT, INT (INTEGER), and BIGINT
		Support functions of year, month, and day. The value entered is converted by the year, month, and day functions. Then, it is compared with the sub-table information.

If the function is empty, the int value is compared directly with the sub-table information.

Example:
If hired is of date type, the corresponding value inserted for query is in the format of '20160101 10:20:20', 20160101
```
	CREATE TABLE employees_int (
	    id INT key NOT NULL,
	    fname VARCHAR(30),
	    lname VARCHAR(30),
	    hired date,
	    separated DATE NOT NULL DEFAULT '9999-12-31',
	    job_code INT,
	    store_id INT
	)
	shardkey=id
	PARTITION BY RANGE ( month(hired) ) (
	    PARTITION p0 VALUES LESS THAN (199102),
	    PARTITION p1 VALUES LESS THAN (199603),
	    PARTITION p2 VALUES LESS THAN (200101)
	);

```
If hired is of int type, the corresponding value inserted for query is in the format of 1474961034. The proxy is converted to the corresponding date format of 20160927, which is then compared with the sub-table information.
```
	CREATE TABLE employees_int (
	    id INT key NOT NULL,
	    fname VARCHAR(30),
	    lname VARCHAR(30),
	    hired int,
	    separated DATE NOT NULL DEFAULT '9999-12-31',
	    job_code INT,
	    store_id INT
	)
	shardkey=id
	PARTITION BY RANGE ( month(hired) ) (
	    PARTITION p0 VALUES LESS THAN (199102),
	    PARTITION p1 VALUES LESS THAN (199603),
	    PARTITION p2 VALUES LESS THAN (200101)
	);

```

Supported list types:
DATE, DATETIME, and TIMESTAMP. Support functions of year, month, and day;
TINYINT, SMALLINT, MEDIUMINT, INT (INTEGER), and BIGINT;
CHAR, VARCHAR, BINARY, and VARBINARY;
```
	CREATE TABLE customers_1 (
	    first_name VARCHAR(25),
	    last_name VARCHAR(25),
	    street_1 VARCHAR(30),
	    street_2 VARCHAR(30),
	    city VARCHAR(15),
	    renewal DATE
	) shardkey=first_name
	PARTITION BY LIST (city) (
	    PARTITION pRegion_1 VALUES IN('1', '2', '3'),
	    PARTITION pRegion_2 VALUES IN('4', '5', '6'),
	    PARTITION pRegion_3 VALUES IN('7', '8', '9'),
	    PARTITION pRegion_4 VALUES IN('10', '11', '12')
	);

```

