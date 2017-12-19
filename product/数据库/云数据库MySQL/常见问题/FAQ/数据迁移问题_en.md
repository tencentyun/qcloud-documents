### 1. How to import local SQL files to the MySQL database?

**Step 1:** At the upper left corner of [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Relational Databases" under the "Cloud Products" menu to go to the database product page.
![Image](http://tss.sng.com/ticket/upload/downloadFile?filename=5982c66ca5c5d.png)
**Step 2:** On the relational database page, click "Instance List" under "MySQL", and then locate the MySQL database instance with a status of "Uninitialized" in the target region (in this example, it is Guangzhou). 
![Image](http://tss.sng.com/ticket/upload/downloadFile?filename=5982c6b80c190.png)
**Step 3:** Click "Initialize" to initialize the MySQL instance.
![Image](http://tss.sng.com/ticket/upload/downloadFile?filename=5982c6cc0cf33.png)
**Step 4:** Configure initialization parameters, and then click "OK" to start initialization.
**Supported character set**: Select the character set supported by the MySQL database.
**Whether table name is case-sensitive**: Specify whether the table name is case-sensitive. Default is "Yes".
**Custom port**: Access port of database. Default is 3306.
**Root account password**: The default user name for the new MySQL database is "root". This is used to set the password of the root account.
**Confirm password**: Enter the password again.
![Image](http://tss.sng.com/ticket/upload/downloadFile?filename=5982c70136d95.png)

**Step 5:** The status of the MySQL instance becomes "**Running**", which indicates it has been initialized successfully.
![Image](http://tss.sng.com/ticket/upload/downloadFile?filename=5982c71f8a223.png)

**Step 6:** Click "Management" in the "Operation" column, click "Import Database", and then select the file to be imported. Next, select the destination database and confirm import (A single SQL file to be imported cannot larger than 2 GB. Letters, numbers and underscores are allowed in the file name).
![Image](http://tss.sng.com/ticket/upload/downloadFile?filename=5982d52b2cb47.png)

### 2. How to export database data?
1. To export cold backup data, download the data in "Backup Management" in the console.
2. To export real-time data, you can purchase read-only instances, and get the data through the read-only instance mysqldump.

### 3. Which is the quickest way to migrate data from the 7-GB source database to the MySQL database purchased from Tencent Cloud?
You're recommenced to use [Data Migration](https://cloud.tencent.com/document/product/571/8710) feature to directly connect to your source database for data synchronization.

### 4. How to achieve the synchronization of real-time data of two instances in a local dual-backup architecture?
For this purpose, you can purchase [Disaster Recovery Instances](https://cloud.tencent.com/document/product/236/7272) in the console.

