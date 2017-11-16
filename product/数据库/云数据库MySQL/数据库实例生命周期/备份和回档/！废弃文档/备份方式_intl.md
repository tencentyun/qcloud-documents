## Backup Methods


#### 1. Physical Backup and Logical Backup
Currently, CDB for MySQL supports two automatic backup methods
1. Physical backup: A full copy of physical data
2. Logical backup: Backup of SQL statements

#### 2. Setting Backup Method
On the instance list page, click an instance, enter "Backup Management", and click "Automatic Backup Setting" to set backup method
![](//mc.qcloudimg.com/static/img/e4c8cefb6dbe8d4bdc2c46848d8c40c9/image.png)
![](//mc.qcloudimg.com/static/img/dcef37daa0e543f3cc6e832994ce06aa/image.png)

#### 3. Notes About Backup Methods
1. For logical backup, downloads at both the instance level and the database table level are supported, while for physical backup, only download at the instance level is supported
2. For the MySQL below version 5.6, only logical backup is supported
