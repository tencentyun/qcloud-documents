## 1. Introduction
Tencent Cloud CDB for MySQL allows users to create one or more read-only instances to support read/write splitting and the "One Master, Multi-Slave" application scenarios, which can significantly improve the read load capability of the user database.

## 2. Glossary
*RO group: read-only instance group with CLB. If there are multiple read-only instances in the RO group, the user's read requests can be evenly assigned to each read-only instance within the group. And RO group provides IP and Port publicly for access to the database.
*Read-only instance: single node (no slave) instance that supports read requests. Read-only instances cannot exist separately, and each read-only instance belongs to an RO group.

## 3. Features 
*A maximum of 3 read-only instances can be created for one master instance (MySQL 5.6 GTID).
*The read-only instance specification is allowed to be different from the master instance, so that upgrade can be made according to the load situation. However, in order to ensure normal synchronization with the master instance, the read-only instance specification needs to be greater than or equal to that of the master instance.
*There is no need to maintain account and database for read-only instances, since they are both synchronized from the master instance.

## 4. Infrastructure
The MySQL binlog master/slave synchronization is made available for read-only instance, allowing the changes to the master instance (source database) to be synchronized to all read-only instances. All read-only instances feature a single-node (excluding the standby machine) architecture and a read-only instance will be back in service within 24 hours after a crash.
![](//mc.qcloudimg.com/static/img/3f2a163d690deda5978474f8db4b8738/image.png)


## 5. Usage Tips and Functional Limits
*"A capacity of 100G and a memory of 4,000 MB" or above is required for the purchase of read-only instances. If you want read-only instances with a specification lower than that, please upgrade the master instance specification first.
*Backup/rollback: backup and rollback are not supported;
*Data migration: data migration to read-only instances is not supported
*Database management: creation or deletion of database is not supported; PMA is not supported
*Account management: creation or deletion of accounts is not supported; authorization to account and modification to account or password are not supported
*Read-only instances can only be enabled for master databases of the MySQL 5.6 (GTID) version. If your MySQL version is lower than 5.6, you can submit a ticket to request for upgrading it to MySQL 5.6 GTID version before you can purchase the read-only instance; if your MySQL version is 5.6 but GTID is not enabled, you can first enable GTID through the console and then add read-only instances. It will take a long time to enable GTID and a few seconds' interruption will happen to the instance, so it is recommended to operate during an off-peak period, and add a reconnection mechanism in the program for accessing the database.
*InnoDB is the only supported engine type for read-only instances, and read-only instances can only be created for master instances with the InnoDB engine. If you create a read-only instance with a database that contains MyISAM tables, MyISAM will be forcibly converted to InnoDB during the creation process.
*Because the data synchronization of read-only instances is based on MySQL native Binlog synchronization, you will no longer be able to set your instances to the Binlog format once the read-only instances are enabled.
*There may be a small amount of data inconsistencies between read-only instances due to data synchronization latency. Synchronization latency between the read-only instances and the master instance can be viewed on the console.
*Read-only instances in the same RO group should have consistent specifications
*Currently, a master instance supports up to three RO groups, each of which supports only a single read-only instance node.

## 6. Purchase and Billing
Read-only instances run on a pay-by-usage billing mode only. Tiered prices are available; the longer the service is used, the more the discount is offered. Refer to the purchase page for more information on tiered prices.

*You access the instance purchase page by going to the instance management page:
	*Step 1. Enter the instance list, and click "Manage"
![](//mc.qcloudimg.com/static/img/5a3e1aca92b6f1fe502a7a2f59b23662/image.png)
	*Step 2. Click "Add Read-only Instance"
![](//mc.qcloudimg.com/static/img/e59eb9fff3b5661bcd548b066c48b280/image.png)
	*Step 3. Click "New"
![](//mc.qcloudimg.com/static/img/38fb7789fa98a7f9e7170e965fce610b/image.png)

*Read-only instance purchase page:
![](//mc.qcloudimg.com/static/img/0b424ba8e67b16b284d51329e77a127b/image.png)
 
## 7. Upgrade
1. To ensure normal synchronization between the master instance and the read-only instances, the specification of the master instance needs to be less than or equal to that of the read-only instance.
2. If the read-only instance is not upgraded along with the upgrade of the master instance, the master instance can only be upgraded to an instance specification that is less than or equal to that of the read-only instance. If there are multiple read-only instances under this master instance, and they have different specifications, the master instance can be upgraded to the lowest specification of these read-only instances.
3. One or more read-only instances can be upgraded along with the upgrade of the master instance. If you select all the read-only instances for upgrade at the same time, you can choose to upgrade to any instance type with a specification larger than the current master instance specification. All read-only instances with a specification lower than that of this instance type will be upgraded, while read-only instances above this specification will neither be upgraded nor degraded. If only part of the read-only instances are selected, the master instance can only be upgraded to an instance specification that is less than or equal to the lowest specification of the unselected read-only instances.

