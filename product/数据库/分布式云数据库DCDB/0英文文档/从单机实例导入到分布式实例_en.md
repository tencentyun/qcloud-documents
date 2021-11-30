## 1. Overview of Data Import
Distributed architecture of distributed database is transparent to users, so generally, you only need to create table structure first. Then you can migrate data using MySQL client, such as mysqldump, Navicat and SQLyog. Procedures of migration are as follows:

Step 1: Prepare import and export environment
Step 2: Export the table structure and data of the source table
Step 3: Modify the statement for creating table and create table structure in the destination table
Step 4: Import data

## 2. Prepare import and export environment
Before migrating data, you need to get the following prepared:

- CVM
	- 2-core CPU, MEM 8 GB, Disk 500 GB+ (depending on data volume) (recommended)
	- Linux
	- MySQL client installed
	- If the data volume is small (<10 GB), you can also import it directly via public network (Internet) with nothing to be prepared.
- DCDB:
	- Select expected volume and make initialization according to the source library character set, table name case status and the value of innodb_page_size.
	- Create an account with all global permissions enabled (recommended)
	- Use public IP if necessary

## 3. Export the table structure and data of the source table
### 3.1 Demonstration environment
- Operating database: caccts
- Operating table: t_acct_water_0
- Source database: single instance mysql
- Destination database: DCDB for Percona, MariaDB

### 3.2 Export table structure in the source database
Execute `mysqldump -u username -p password -d dbname tablename > tablename.sql` to export table structure

```
//Command example
mysqldump -utest -ptest1234 -d -S /data/4003/prod/mysql.scok caccts t_acct_water_0 > table.sql
```
### 3.2 Export table data in the source database

Execute `mysqldump -c -u username -p password dbname tablename > tablename.sql` to export table structure

```
//Command example
mysqldump -c -t -utest -ptest1234 -S /data/4003/prod/mysql.scok caccts t_acct_water_0 > data.sql
```

> Note: Data must be exported through mysqldump with parameter -c in order to get data with column name field. Sql without column name field will not be accepted by DCDB for Percona and MariaDB. Parameter -t specifies that only table data will be exported and table structure will not.

### 3.3 Upload files to a directory on CVM
Before uploading, you need to enable CVM public IP and read the CVM file upload guideline: [File Upload from Linux Machine Using SCP](https://cloud.tencent.com/document/product/213/2133). You should upload at least the following exported contents:
- Table structure sql: table.sql
- Data sql: data.sql

## 4. Modify the statement for creating table and create table structure in the destination table
Open the exported table structure file table.sql, add primary key and shardkey through statements like the followings, and save as tablenew.sql. Pay attention to [shardkey selection techniques and notes]():
```CREATE TAbLE (
	column name 1 data type,
	column name 2 data type,
	column name 3 data type,
	...,
	PRIMARY KEY('column name n'))
	ENGINE=INNODB DEFAULT CHARSET=xxxx 
	shardkey=keyname
```

>Note: Primary key and shardkey must be set. Pay attention to the table name case status. It is recommended to delete redundant notes, or the table may not be created.

![](https://mc.qcloudimg.com/static/img/1cd921ececbacf81226a69a0eb5b919a/image.png)

## 5. Import data
### 5.1 Connect to DCDB for Percona and MariaDB instance
On CVM, use `mysql -u username -p password -h IP -P port `to log in to MySQL server, and use `use dbname` to enter the database.

> Note: You may need to create a database first.

### 5.2 Import table structure
Use the uploaded file and import data with `source` command.

1. Import table structure: `source /file path/tablenew.sql`
2. Import data: `source /file path/data.sql`
3. Verify the import result: `select count(*) from tablename`

> Note: You need to import table creation statement before importing data. You can also import sql directly using the source command in mysql.

## 6. Others
Generally, you can import data smoothly as long as you have created the corresponding table structure with shardkey specified in the destination table before importing data.
