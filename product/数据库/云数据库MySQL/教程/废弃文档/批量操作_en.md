## 1 Batch Renewal
### 1.1 Performing Batch Renewal with the Console

Step 1. Select one or more instances that require renewal and click "Batch Renewal".

![](//mccdn.qcloud.com/img56825d68b83d4.png)

Step 2. Select the renewal length, and click "OK" to continue.

![](//mccdn.qcloud.com/img56825d6f7b8c5.png)

Step 3. After confirming the order information, click "Confirm the Payment".

![](//mccdn.qcloud.com/img56825d763f318.png)

Step 4. Once the order has been paid, you can continue to view the order or jump to the Console.

![](//mccdn.qcloud.com/img56825d7c5d5ea.png)

## 2 Batch Rollback

### 2.1 General Instructions

Users can roll back the database or table in the Tencent Cloud platform.

Rollback is based on cold backup+binlog, and data can be rolled back in real time.

The cloud database rollback tool can roll back the cloud database or table to the specified time with regular images and real-time flow reconstruction, and ensure that all data have the same time slice.

It will not affect the access of original database or table; the rollback operation will generate a new database or table. After the rollback is finished, the user can see the original database or table, as well as the new database or table.

> Note: Cloud database will not change any user data. The data damage due to personal cause can be repaired through rollback.
>
### 2.2 Performing Batch Rollback with the Console

Step 1. Select one or more instances that require rollback and click "Batch Rollback".

![](//mccdn.qcloud.com/img56825d2d97ec4.png)

Step 2. Specify the database tables that need to be rolled back for each instance.

![](//mccdn.qcloud.com/img56825d1ff334a.png)


Step 3. Specify the name after rollback and the rollback time, and click "Perform Rollback". Once the submission is successful, the list of tasks performed on the cloud database will be displayed, and you can view the rollback progress.

![](//mccdn.qcloud.com/img56825d17d8e14.png)

![](//mccdn.qcloud.com/img56825d12ea040.png)

Step 4. Find the rollback instance and click "Manage" in the "Operation". After entering the instance page, click "Operation Log" and select "Rollback Log" to view rollback history and current progress.

![](//mccdn.qcloud.com/img56825d075c08a.png)

## 3 Batch SQL Operations

### 3.1 General Instructions

This function allows you to execute SQL statements on multiple instances or databases selected. You can use this function to create database/table and change table structure in batches to complete initialization or modification of multiple instances. In order to use this function, you need to ensure that the user name/password of the selected instances is consistent.

3.1.1 Generating the SQL files to be executed

The SQL files to be executed can be generated in the following two ways:
<span style = "color:#F00"> Note: It is not recommended to manually construct SQL files, because the manually constructed SQL files are prone to have errors on syntax, data and so on, which may result in execution failures. </span>
Method 1:  Files exported by the export function in the cloud database console (For details, see: [Cold Backup Data Extraction](/doc/product/236/冷备数据提取));

Method 2: Data files exported by the MySQL tool mysqldump:

(1) The data files exported by mysqldump must be compatible with the SQL standard of the purchased cloud database's MySQL version. You can log in to the cloud database via select version (); to obtain corresponding MySQL version information.

(2) The data export method for mysqldump is as follows:

shell> mysqldump [options] db_name [tbl_name ...]
Options are the export options, db_name is the database name, and tbl_name is the table name.
For more details on mysqldump data export, please refer to [MySQL Official Manual](http://dev.mysql.com/doc/refman/5.1/en/mysqldump.html).

3.1.2 Restrictions on the SQL files to be executed

The total size of the files that execute SQL statement cannot exceed 2 MB. SQL files only support reuse in the same region. Please re-upload the files when used in a new region.

3.1.3 Character set encoding issues of the SQL files to be executed

1. If the SQL files to be executed do not specify a character set encoding, the one set by the cloud database will be executed.
2. If the SQL files to be executed have specified a character set encoding, the specified one will be executed.
3. If the character set encoding of the SQL files to be executed is different from those of the cloud database, it will display unreadable codes.
For more information about character set encoding issues, please refer to "#6. Character Set" in "Service Limits".

3.2 Performing Batch SQL Operations with the Console

Step 1. Select one or more instances that require SQL operations and click "Batch SQL Operations".

![](//mccdn.qcloud.com/img56825e5e779b7.png)

Step 2. Select the instance or database to be operated, and click "Next" to continue.

![](//mccdn.qcloud.com/img56825e584c1cb.png)

Step 3. Select the SQL file. If you cannot find the required SQL file, click "Add File" to upload.

![](//mccdn.qcloud.com/img56825e4c63c6a.png)

Step 4. Confirm the instance or database to be operated as well as the SQL files. Then, enter the user name and password if all information is correct, and then click "Next" to continue.

![](//mccdn.qcloud.com/img56825e4227d88.png)

Step 5. After the operation is submitted, you can view the task information, and view the progress of the task if needed. You can click "Cancel Task" before the task is completed.

![](//mccdn.qcloud.com/img56825e3723afa.png)



