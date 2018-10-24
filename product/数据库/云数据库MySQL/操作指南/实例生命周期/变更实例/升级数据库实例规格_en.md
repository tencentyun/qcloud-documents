## 1. How to upgrade the cloud database instance specification by yourself?
Log in to the cloud database [Management Console](https://console.cloud.tencent.com/cdb) and upgrade the specified instance specification through [Upgrade] operation.
![Upgrade][image-1]
## 2. Instance maintenance duration
The maintenance duration can be set for each instance. Changes to database instances are usually involved in maintenance (such as instance specification upgrades, database version upgrades, etc.). It is recommended to set the maintenance duration of the database in the off peak hours of transactions.
Let's take the database instance specification upgrade as an example. Because the instance specification upgrading involves data migration, after upgrading is completed, flash disconnection within seconds may occur to MySQL database. When upgrading is initiated, the switching time can be selected as ''Within maintenance duration", so that the switching will be enabled in the next "Maintenance duration" after the instance upgrading is completed.
It should be noted that when the switching time is selected as the [Within maintenance duration], the switching action will not occur immediately after the database specification upgrading is completed. It will keep synchronized till the time goes "Within maintenance duration" After that, the switching action will be enabled. In this way, the whole instance upgrading time may be extended.

### Set an instance maintenance duration
"Instance Details">"Maintenance Duration">"Modify"
![Maintenance Duration][image-2]
![Modify Maintenance Duration][image-3]

### Settings of the switching time for upgrading
The switching time has two options as follows:
* After the upgrading is complete: After the instance has been upgraded, switching is initiated immediately, during which flash disconnection may occur to the database within seconds. In this way, the entire upgrading process will take the shortest time, but the flash disconnection time is completely out of control.
* Within the maintenance duration: The switching action will not occur immediately after the database specification upgrading is completed. It will keep synchronized till the time goes "Within maintenance duration". In this way, the flash disconnection within seconds after the end of the database upgrading can be placed within the controllable maintenance duration, but the time required for the instance upgrading may be extended.

![Settings of the switching time for upgrading][image-4]

## 3. How to Calculate Fees
For prepaid instances, when the user is upgrading database instances, the system will calculate the price difference between instance specifications, and this price difference will be deducted from the user's account. The user will need to top up first if there isn't enough balance in the account. After upgrading, the fees will be calculated based on the new instance specification.
For postpaid instances, after the instances are upgraded, the fees will be calculated in next billing period based on the new instance specifications.

## 4. Restrictions When Upgrading Instance Specifications by Yourself
* Instance specification self-upgrading function is only available to prepaid and postpaid users.
* You can only upgrade instances from smaller specifications into larger ones. **Degrading is not supported**.
* You can only upgrade an instance when it is in upgradeable status. For an instance that is currently being upgraded, you will have to wait for the upgrade process to be completed before upgrading it again.
* You are not allowed to cancel the upgrade process once it has started.

## 5. NoteS
1. You can still use the original instance as usual during the upgrading process (for example, importing or exporting data).
2. The name, access IP and access port of the instance will not change after the instance is upgraded.
3. **When the upgrading process is completed, the MySQL database connections will be disconnected within seconds. It is recommended that applications are configured with auto reconnect feature.**
4. **During upgrading process, please try to avoid operations such as modifying the global parameters of MySQL, instance name and user password.**

[image-1]:	//mccdn.qcloud.com/static/img/d7b59861436817bcc9a0be795c49b1ec/image.png
[image-2]:  //mc.qcloudimg.com/static/img/da7f29b04e72c26bac1ddaeaf1d90eed/1.png
[image-3]:  //mc.qcloudimg.com/static/img/bbdebbe19bd1ef5e85d997d5de6a2e06/2.png
[image-4]:  //mc.qcloudimg.com/static/img/bf9bb0a92ba480690c86080161a3c9bc/3.png

