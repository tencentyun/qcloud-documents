To connect to a CDB for MariaDB (TDSQL) instance, you should "create an account" and "obtain an instance address".


### 1.Select account management on the account management page
Before using MariaDB (TDSQL) service, you need to enter the management page of MariaDB (TDSQL) instance to create a database account for logging in to MariaDB (TDSQL), and set the access permissions.
![](//mccdn.qcloud.com/img56835afdde2f1.png)

You can see "Account Management" on the management page, as shown below:
![](//mccdn.qcloud.com/img56835b1a37efe.png)
### 2.Create an account
The account consists of a username, CVM IP, and password;

-  **Username**: It should be a combination of letters, numbers and underscores with a maximum length of 16 characters, and begin with a letter and end with a letter or number;
-  **CVM IP**: It can be regarded as HOST IP. IP, IP segment, and % are supported. % means all of the IP addresses within a range. For example, if CVMs in the IP range of 10.10.10.1 - 10.10.10.254 are supported, enter 10.10.10.% instead of codes
-  **Whether it is read-only account**: If you check this option, the account can only use read-only request (select);
-  **Password**: It contains 8 to 16 characters, including letter, numbers and symbols, and requires periodic change.

![](//mccdn.qcloud.com/img56835b84c71c7.png)

>Note: You need to set permissions for different CVM IPs under the same account separately. For a CVM IP to be given permissions similar to those of any one under the same account, select "Clone" in the Account Management to quickly clone the account number and permissions.

### 3.Set permissions
The permissions of MariaDB (TDSQL) are defined at the object level, including 19 permissions of database. You can also set permissions for objects such as tables, views, functions and triggers.
![](//mccdn.qcloud.com/img56835bf828954.png)
>Note: You need to create a database before setting the object-level permissions.

### 4.Limits
Due to limits of design ideas and information security requirements, the account cannot be created or modified through command lines `insert into mysql.user`, `grant`, `drop` currently.


