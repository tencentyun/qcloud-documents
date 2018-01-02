### 1. How to configure backup for MySQL manually?
You can back up your MySQL data by migrating the data to local machine offline. For more information, please see [Migrating Data Offline](https://cloud.tencent.com/document/product/236/8464).

### 2. How can developers back up data?
Cloud database instances are fully backed up every day. Developers can also back up data using the quick multi-thread import/export tool provided by the cloud database (For more information, please see [Manual Backup and Recovery of Cloud Database](https://cloud.tencent.com/document/product/236/7275)), or using the mysqldump tool.

### 3. How to set backup method for MySQL?
On the instance list page, click an instance to go to "Backup Management", and then click "Automatic Backup Settings" to set backup method.
![](//mc.qcloudimg.com/static/img/61eec4f474762057d6956dc61ecc1214/image.png)
![](//mc.qcloudimg.com/static/img/d67376cc5c98175d31fd29ae55499cb9/image.png)

### 4. What backup methods does MySQL support?
4.1. For logical backup, downloads at both the instance level and the database table level are supported, while for physical backup, only download at the instance level is supported.
4.2. MySQL below 5.6 only supports logical backup.

### 5. Where is the backup database in MySQL async replication mode?
Cloud database instances are fully backed up every day. Developers can download backup data in the console via public network or private network, or back up database manually in phpMyAdmin.

### 6. How to view the binlog in MySQL?
6.1 Download binlog from the console to the local machine, for example, to the CVM.
6.2. View the binlog using mysqlbinlog command. ForMySQL 5.6, mysqlbinlog 3.4 or above is required for you to view the binlog on local server.

### 7. How long is the binlog of cloud database retained?
MySQL binlog takes up a large amount of storage space, thus the cloud database only retains the binlog for the last five days. In addition, if the data volume of binlog grows so fast that the server disk storage is not enough to store the binlog for five days, you need to delete binlog manually to free the storage space. For more information, please see <a href="https://cloud.tencent.com/document/product/236/7269#5-.E4.BA.91.E6.95.B0.E6.8D.AE.E5.BA.93.E7.9A.84binlog.E4.BF.9D.E5.AD.98.E6.97.B6.E9.97.B4.E8.AF.B4.E6.98.8E5" target="_blank">binlog storage duration of cloud database</a>.




