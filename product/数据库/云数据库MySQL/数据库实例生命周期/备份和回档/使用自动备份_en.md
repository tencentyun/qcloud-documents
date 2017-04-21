# Working with Automatic Backup


#### 1 Automatic Backup Methods
Currently, CDB for MySQL supports two automatic backup methods:

1. Physical backup: A full copy of physical data (test invitation is going on)

2. Logical backup: Backup of SQL statements

#### 2. Setting Backup Method
On the instance list page, click an instance, enter "Backup Management", and click "Automatic Backup Setting" to set backup method
![][image-1]
![][image-2]

#### 3. Notes About Backup Methods
1. For logical backup, downloads at both the instance level and the database table level are supported, while for physical backup, only download at the instance level is supported
2. For the MySQL below version 5.6, only logical backup is supported



[image-1]:	https://mc.qcloudimg.com/static/img/61eec4f474762057d6956dc61ecc1214/B1.png
[image-2]:	https://mc.qcloudimg.com/static/img/b9d7e7a4297ae93b6ada3a40cfc618b0/111.png
