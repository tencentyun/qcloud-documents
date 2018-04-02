## 1. How to upgrade the cloud database instance specification by yourself?
Log in to the cloud database [Management Console](https://console.cloud.tencent.com/cdb) and upgrade the specified instance specification through **Upgrade** operation.
![](//mc.qcloudimg.com/static/img/fc4c90d73d23c5218b881b31f57eb13d/image.png)
## 2. Instance maintenance duration
The maintenance duration can be set for each instance. Changes to database instances are usually involved in maintenance (such as instance specification upgrades, database version upgrades, etc.). It is recommended to set the maintenance duration of the database in the off peak hours of transactions.
Let's take the database instance specification upgrade as an example. Because the instance specification upgrading involves data migration, after upgrading is completed, flash disconnection within seconds may occur to MySQL database. When upgrading is initiated, the switching time can be selected as ''Within maintenance duration", so that the switching will be enabled in the next "Maintenance duration" after the instance upgrading is completed.
It should be noted that when the switching time is selected as the [Within maintenance duration], the switching action will not occur immediately after the database specification upgrading is completed. It will keep synchronized till the time goes "Within maintenance duration" After that, the switching action will be enabled. In this way, the whole instance upgrading time may be extended.

### Set an instance maintenance duration
"Instance Details">"Maintenance Duration">"Modify"
![](//mc.qcloudimg.com/static/img/6267d39ea7cf9cb554f5794bede6ed4f/image.png)
![](//mc.qcloudimg.com/static/img/1fc4249721bd990e0191af452527ed09/image.png)

### Settings of the switching time for upgrading
The switching time has two options as follows:
* After the upgrading is complete: After the instance has been upgraded, switching is initiated immediately, during which flash disconnection may occur to the database within seconds. In this way, the entire upgrading process will take the shortest time, but the flash disconnection time is completely out of control.
* Within the maintenance duration: The switching action will not occur immediately after the database specification upgrading is completed. It will keep synchronized till the time goes "Within maintenance duration". In this way, the flash disconnection within seconds after the end of the database upgrading can be placed within the controllable maintenance duration, but the time required for the instance upgrading may be extended.

![](//mc.qcloudimg.com/static/img/c98427bda52b433159fbf036cc8dd9fd/image.png)

## 3. How to Calculate Fees
After the instances are upgraded, the fees will be calculated in next billing period based on the new instance specifications.

## 4. Restrictions When Upgrading Instance Specifications by Yourself
* You can only upgrade instances from smaller specifications into larger ones. **Degrading is not supported**.
* You can only upgrade an instance when it is in upgradeable status. For an instance that is currently being upgraded, you will have to wait for the upgrade process to be completed before upgrading it again.
* You are not allowed to cancel the upgrade process once it has started.

## 5. Notes
1. You can still use the original instance as usual during the upgrading process (for example, importing or exporting data).
2. The name, access IP and access port of the instance will not change after the instance is upgraded.
3. **When the upgrading process is completed, the MySQL database connections will be disconnected within seconds. It is recommended that applications are configured with auto reconnect feature.**
4. **During upgrading process, please try to avoid operations such as modifying the global parameters of MySQL, instance name and user password.**



