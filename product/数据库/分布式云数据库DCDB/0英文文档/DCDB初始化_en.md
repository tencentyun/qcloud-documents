Here is the specific operation flow of DCDB instance initialization.
## DCDB Console
1. Log in to the [Console](https://console.cloud.tencent.com/) and move the mouse cursor to "Cloud Products" > "Basic Products" > "Database", and then click "Distributed Database" to enter [DCDB Console](https://console.cloud.tencent.com/dcdb).
	![](https://mc.qcloudimg.com/static/img/23475689f7192fd8a0fc681d9e4cea2e/r1.png)
2. In the console, you can see the created but not initialized DCDB instance, click "Initialize" on the right of the instance.
	![](https://mc.qcloudimg.com/static/img/3f1382a09e8636e052ca766e71d40465/image.png)

3. In the pop-up instance initialization interface, select the configuration as needed and click "OK" to initialize.
 - Supported character set: Select the character set supported by the MySQL database.

 - Table name is case sensitive: Set whether the table name of database is case sensitive.

	-  Enable strongsync: Enable strongsync to ensure consistency of slave data when a master fails. At least two nodes are required to run normally. It is not enabled by default, that is, data sync mode is async.

	- innodb_page_size: The value is Innodb index page length, and the default value for MariaDB is 16K. Modifying this value will affect index creation. The smaller the value, the better the performance. But changing it to 4 KB will result in that a single index can not exceed 768 bytes.
	
	![](https://mc.qcloudimg.com/static/img/6f9711414968945d27a8533c914e0317/r3.png)
	
4. Waiting for about two minutes, the instance status is converted to "running", indicating that the initialization is complete, and you can connect the database for the next step.
	![](https://mc.qcloudimg.com/static/img/87b5573dc8220c19069aa8d8b08cbcb3/r4.png)
