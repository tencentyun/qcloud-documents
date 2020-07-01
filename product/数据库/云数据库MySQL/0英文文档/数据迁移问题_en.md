### 1. How to import local SQL files to the MySQL database?

**Step 1:** At the upper left corner of [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Relational Databases" under the "Cloud Products" menu to go to the database product page.
![](//mc.qcloudimg.com/static/img/511cad3621447b36d204b87bf83bb09f/image.png)
**Step 2:** On the relational database page, click "Instance List" under "MySQL", and then locate the MySQL database instance with a status of "Uninitialized" in the target region (in this example, it is Guangzhou). 
![](//mc.qcloudimg.com/static/img/bc6f4a538ac4bf614e3a270338a7be4c/image.png)
**Step 3:** Click "Initialize" to initialize the MySQL instance.
![](//mc.qcloudimg.com/static/img/fe0ebd9776b6f920338e9436b82024a3/image.png)
**Step 4:** Configure initialization parameters, and then click "OK" to start initialization.
**Supported character set**: Select the character set supported by the MySQL database.
**Whether table name is case-sensitive**: Specify whether the table name is case-sensitive. Default is "Yes".
**Custom port**: Access port of database. Default is 3306.
**Root account password**: The default user name for the new MySQL database is "root". This is used to set the password of the root account.
**Confirm password**: Enter the password again.
![](//mc.qcloudimg.com/static/img/a1b69801dc18d284ef8b0f3ea777265b/image.png)

**Step 5:** The status of the MySQL instance becomes "**Running**", which indicates it has been initialized successfully.
![](//mc.qcloudimg.com/static/img/81234ad724b600506564d920b051ce3f/image.png)

**Step 6:** Click "Management" in the "Operation" column, click "Import Database", and then select the file to be imported. Next, select the destination database and confirm import (A single SQL file to be imported cannot larger than 2 GB. Letters, numbers and underscores are allowed in the file name).
![](//mc.qcloudimg.com/static/img/5cf4795c885ea7a699dcf5b94a4a725e/image.png)

### 2. How to export database data?
1. To export cold backup data, download the data in "Backup Management" in the console.
2. To export real-time data, you can purchase read-only instances, and get the data through the read-only instance mysqldump.

### 3. Which is the quickest way to migrate data from the 7-GB source database to the MySQL database purchased from Tencent Cloud?
You're recommenced to use [Data Migration](https://cloud.tencent.com/document/product/571/8710) feature to directly connect to your source database for data synchronization.

### 4. How to achieve the synchronization of real-time data of two instances in a local dual-backup architecture?
For this purpose, you can purchase [Disaster Recovery Instances](https://cloud.tencent.com/document/product/236/7272) in the console.
