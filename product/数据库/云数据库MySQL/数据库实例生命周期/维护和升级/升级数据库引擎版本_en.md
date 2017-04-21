CDB supports in-place upgrade for MySQL database engines of the following major versions:
* From MySQL 5.5 to MySQL 5.6

CDB for MySQL does not support cross-major version upgrade. If you wish to upgrade the database instance of major version MySQL 5.1 on CDB to MySQL 5.6 or above, you will need to upgrade the database instance to MySQL 5.5 first.

During the upgrade process of MySQL major version, the CDN will clear the slow\_log table. Please save the contents of the log before upgrading the major version if you wish to keep your log information. The major version upgrading process of CDB for MySQL usually takes a long time.

#### Note
The master-slave synchronization feature of CDB for MySQL 5.6 is achieved based on GTID and only supports InnoDB engine by default. Therefore you need to note the following about the upgrade:
* The table of MyISAM engine will be converted to InnoDB during upgrade;
* `create table ...  as select ... ` syntax is not supported;
* Is it recommended that you complete the MyISAM-to-InnoDB conversion operation before upgrading.

#### Console Upgrade
1. In the instance list or instance detail screen, click "Upgrade" behind the instance that you wish to upgrade.
	![][image-1]
2. Select the desired database version from "Database Version" and click "Upgrade".
	![][image-2]

[image-1]:	//mc.qcloudimg.com/static/img/f4eaf9b29aab12a0ae7547e858c68951/image.png
[image-2]:	//mc.qcloudimg.com/static/img/b84f5f33e1687d22b543cef8d7e391eb/image.png
