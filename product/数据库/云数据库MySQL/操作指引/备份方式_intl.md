## Backup Methods


#### 1. Physical Backup and Logical Backup
Currently, CDB for MySQL supports two automatic backup methods
1. Physical backup: A full copy of physical data
2. Logical backup: Backup of SQL statements

#### 2. Setting Backup Method
On the instance list page, click an instance, enter "Backup Management", and click "Automatic Backup Setting" to set backup method
![](https://mc.qcloudimg.com/static/img/61eec4f474762057d6956dc61ecc1214/B1.png)
![](https://mc.qcloudimg.com/static/img/d67376cc5c98175d31fd29ae55499cb9/B2.png)

#### 3. Notes on Backup Methods
1. For logical backup, downloads at both the instance level and the database table level are supported, while for physical backup, only download at the instance level is supported
2. For the MySQL below version 5.6, only logical backup is supported



