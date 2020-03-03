
This tutorial shows how to create a SQL Server cloud database instance, and connect to the database instance and run simple queries through SQL Server Management Studio (SSMS) in Windows CVM, and finally, delete the database instance.
If you want to connect to a SQL Server cloud database locally using SQL Server Management Studio (SSMS), refer to [Create and Connect to a SQL Server Cloud Database (Local)](/doc/product/238/11627).

> **Note:**
> You must have a Tencent Cloud account to create a SQL Server cloud database instance. If not, please fill out the relevant information in [Registration Page](https://cloud.tencent.com/register) to register a Tencent Cloud account.

## Creating a SQL Server Cloud Database Instance
Next we will show you how to create a database instance using the Tencent cloud console.
1. Log in to the [Cloud Database Console](https://console.cloud.tencent.com/cdb).
![](//mc.qcloudimg.com/static/img/7f454c8f988ec22c4045b33c47571024/image.png)
2. Select the type of cloud database to be created in the right navigation bar (here is SQL Server). Click "+ New" to enter purchase page of the cloud database SQL Server.
![](//mc.qcloudimg.com/static/img/798911fbe873e0a59de7d749b365c0ca/image.png)
3. In the purchase page of cloud database SQL Server, select the corresponding database configurations, and then click "Buy Now" after confirmation.
 - Billing method: Now, only prepaid mode is supported.
 - Regions and Availability Zones: Here we take "Guangzhou" and "Guangzhou zone 3" as examples. For more information on regions, see [Regions and Availability Zones](/doc/product/236/8458).
 - Network environment: Basic network and private network are supported. Here we take "basic network" as an example. For the difference between VPC and basic network, see [Network Environment](/doc/product/213/5227).
 - Database Version: SQL Server 2008 R2 and SQL Server 2012 are supported. It may vary based on actual available zones. Here we take "SQL Server 2012" as an example.
 - Instance specifications and the required disk.
 - Quantity and duration.
![](//mc.qcloudimg.com/static/img/1630495ca9ca9001b4cdef32e1b85364/image.png)
4. Go to [Cloud Database Console](https://console.cloud.tencent.com/cdb) and select "SQL Server" to view the created cloud database instance. If its status is **Running**, the cloud database SQL Server is created successfully.
![](//mc.qcloudimg.com/static/img/eedd98d6992bdb6e06d25d8380365e89/image.png)
5. In the SQL Server cloud database management interface, click "Management" to go to the SQL Server cloud database instance details page.
![](//mc.qcloudimg.com/static/img/aeb4d8c1b053c4ea9dbb6f5a9a48fc4d/image.png)
6. On the SQL Server cloud database instance details page, click "Account Management" -> "Create Account", and the account creating page pops up. Fill in the relevant information and click "OK" after confirmation. **The account and password filled in this step will be used to connect to SQL Server cloud database, so make sure to keep them properly.** Here we take "test" as an example.
![](//mc.qcloudimg.com/static/img/1cac253d8eb9029bbaf10aa385b4c0bd/image.png)
7. On the SQL Server cloud database instance details page, click "Database Management" -> "Create Database", and the database creating page pops up. Fill in the relevant information and click "OK" after confirmation. **Read-write permission** or **read-only permission** is granted to the account created in step 6.
![](//mc.qcloudimg.com/static/img/8db9f2aaa65978c0e0005739c7861aad/image.png)

## Connecting to SQL Server Cloud Database Instance (Windows CVM)
1. Log in to Tencent Windows CVM. If you do not have any Tencent Windows CVM, refer to [Getting Started with Windows CVM](/doc/product/213/2764). Here we take 64-bit Windows Server 2012 R2 Standard as an example.
2. Download and install [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms) in the Tencent Windows CVM. For more documentation on SQL Server Management Studio, refer to the official Microsoft document [Use SQL Server Management Studio][1].
3. On the SQL Server cloud database instance details page, click "Instance Details" to view the private IP and port number of SQL Server cloud database instance. **The private IP and port number are used when connecting to the cloud database.**
![](//mc.qcloudimg.com/static/img/6dcf51fc839f1ea7c47c26609b711ede/image.png)
4. Start SQL Server Management Studio on the Windows CVM. On **Connect to server** interface, fill in the relevant information and click "Connect", then SQL Server Management Studio will connect to your database instance a few minutes later.
![](//mc.qcloudimg.com/static/img/1cac47c4fc515d30d2cb5a0ef0141e22/image.png)
 - Server type: Select Database Engine.
 - Server name: Type or paste the private IP and port number of the database instance, separated by **comma**. For example, if the private IP and port number obtained in step 3 is `10.10.10.10:1433`, then enter `10.10.10.10,1433` here. Make sure to use **English punctuations**.
 - Authentication: Select SQL Server Authentication.
 - Login and Password: Enter the account and password filled in step 6 of chapter 1 when creating your account. Here we take "test" as an example.
5. After connecting to the database, you can view the standard built-in SQL Server databases (master, model, msdb and tempdb).
![](//mc.qcloudimg.com/static/img/a39d9db6f6a4050d1fa4285a53b55157/image.png)
6. Now you can start to create your own database and run queries on the database. Click "File" -> "New" -> "Query with Current Connection", and type the following SQL query statement:
```
select @@VERSION
```
Run the query. SQL Server Management Studio will return Tencent cloud database instance of SQL Server version.
![](//mc.qcloudimg.com/static/img/fbf64c03c7addda9c80fdd3dac7bbebb/image.png)

## Deleting a SQL Server Cloud Database Instance
1. On the SQL Server cloud database instance details page, click "Account Management" -> "Delete Account". It takes time to delete an account. Please wait patiently.
![](//mc.qcloudimg.com/static/img/7ce670ca67766ed32d088b4f733c56b6/image.png)
2. On the SQL Server cloud database instance details page, click "Database Management" -> "Delete". It takes time to delete a database. Please wait patiently.
![](//mc.qcloudimg.com/static/img/fa68b790fe7a12e1c17bfde648ac6e98/image.png)
3. Now manual deletion is not supported for SQL Server cloud database instances. The instance automatically stops if there is no renewal after expiration.

[1]:https://msdn.microsoft.com/zh-cn/library/ms174173(v=sql.105).aspx

