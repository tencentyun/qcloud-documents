### Description
The backup setting function is currently under the public trial, [Application Address](https://cloud.tencent.com/act/apply/cdbpb)
Non-physical backup test users only support logical backup, so they cannot set the backup mode via the [Set Automatic Backup] function.

#### 1. Physical Backup and Logical Backup
For now, CDB for MySQL supports two automatic backup methods
1. Physical backup: A full copy of physical data
2. Logical backup: Backup of SQL statements

#### 2. Setting Backup Method
On the instance list page, click an instance, enter "Backup Management", and click "Automatic Backup Setting" to set backup method
![](https://mc.qcloudimg.com/static/img/61eec4f474762057d6956dc61ecc1214/B1.png)
![](https://mc.qcloudimg.com/static/img/d67376cc5c98175d31fd29ae55499cb9/B2.png)

#### 3. Notes About Backup Methods
1. For logical backup, downloads at both the instance level and the database table level are supported, while for physical backup, only download at the instance level is supported
2. For the MySQL below version 5.6, only logical backup is supported

#### 4. Data Backup Retention
For now, the data backup is free of charge and the backup retention time is 7~732 days. For information about follow-up backup space charges, it will be announced additionally.

#### 5. Start Time
You can set your customized daily backup start time, and the default start time is between 2am to 6am. It should be noted that the backup completion time is affected by the data volume stored in the instance, so the backup may not be completed within the selected period.

#### 6. Manual Backup
The [Manual Backup] function on the upper right corner of the instance allows users to initiate a backup task by themselves. For information about follow-up backup space charges, it will be announced additionally.
It should be noted that multiple backup tasks cannot be initiated at the same time. If the manual backup has not been completed within the specified automatic backup start period, it may affect the automatic backup task initiating time.
