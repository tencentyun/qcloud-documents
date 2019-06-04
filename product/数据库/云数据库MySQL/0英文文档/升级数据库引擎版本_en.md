CDB supports in-place upgrade for MySQL database engines of the following major versions:
* From MySQL 5.5 to MySQL 5.6
* From MySQL 5.6 to MySQL 5.7

CDB for MySQL does not support cross-major version upgrade. For example, if you wish to upgrade the database instance of major version MySQL 5.1 on CDB to MySQL 5.6 or above, you will need to upgrade the database instance to MySQL 5.5 first.

During the upgrading process of major version MySQL, the CDB will clear the slow\_log table. Please save the contents of the log before upgrading the major version if you wish to keep your log information. The major version upgrading process of CDB for MySQL usually takes a long time.

#### Note
The master-slave synchronization function of CDB for MySQL 5.6/5.7 is achieved based on GTID and only supports InnoDB engine by default. Therefore you need to note the following about the upgrade:
* The table of MyISAM engine will be converted to InnoDB during upgrade.
* `create table ...  as select ...` syntax is not supported.
* It is recommended that you complete the MyISAM-to-InnoDB conversion operation before upgrading.

#### Console Upgrade
1. In the Instance Details, click the "Upgrade" button behind the instance database version to be upgraded (MySQL 5.7 cannot be upgraded to a higher version, so no "Upgrade" button is available).
![][image-1]
2. In the "Database Version" option, select the desired database version, and then click "Upgrade". Because the database version upgrading involves data migration, after upgrading is completed, flash disconnection within seconds may occur to MySQL database. When upgrading is initiated, the switching time can be selected as ''Within maintenance duration", so that the switching will be enabled in the next "Maintenance duration" after the instance upgrading is completed.
It should be noted that when the switching time is selected as the [Within maintenance duration], the switching action will not occur immediately after the database specification upgrading is completed within the maintenance interval, the database specification does not switch immediately after the upgrade is completed. It will keep synchronized till the time goes "Within maintenance duration" After that, the switching action will be enabled. In this way, the whole instance upgrading time may be extended.
For more information about how to set the switching time, please see [Description on the switching time when upgrading database specifications](https://cloud.tencent.com/document/product/236/7271).
![][image-2]

[image-1]:	//mc.qcloudimg.com/static/img/30eb65a62102eea61a48422a404df814/4.png
[image-2]:	//mc.qcloudimg.com/static/img/a4b395e9a85a4a289b016cf2ae1c4a14/5.png

