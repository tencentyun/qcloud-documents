Data synchronization can be used for sync disaster recovery instances. This section introduces data synchronization feature with disaster recovery instance as an example.

## Overview
For application with a strong demand for continued services and reliable data or regulatory requirements, TencentDB provides disaster recovery instances to help users enhance their capability to deliver continued services at a low cost and improve data reliability.


## Characteristics
* With a separate database connection address, disaster recovery instances can offer read access capability for such scenarios as "connection to the nearest node" and data analysis with a lower cost in device redundancy.
* Highly available Master/Slave architecture can avoid the single point of failure (SPOF) risks of database.
* Billing on an hourly basis supports instant-on and instant-off. Adoption of tiered prices allows a lower cost for a longer usage.
* **Disaster recovery instance synchronization achieved through private network Direct Connect has a lower synchronization latency and higher stability, with the synchronization linkage being much more superior than the public network.**
* Direct Connect is free of charge during promotion period, and the date of commencement for commercial charges will be subject to the further notice.



## How Does It Work
* In a scenario where a Tencent Cloud database is used as a disaster recovery database, disaster recovery instance is the backup of the master instance database.	
* When any changes take place in the master instance, the log information recording the modification will be copied to the disaster recovery instance, and data synchronization can be achieved through log replay.
* If any failure occurs with the master instance, the disaster recovery instance can be activated in seconds for restoring the full read and write features.

## Preconditions
Before creating a disaster recovery instance, make sure that the master instance is MySQL 5.6 version or above and the GTID feature has been enabled.

## Use Limits
* Disaster recovery instance does not support the following features: transferring project, rollback, SQL operation, parameter settings, changing character set, account management, changing port change, data import, rollback log, read-only instance.

## Procedure
### Purchase a disaster recovery instance
Step 1: In the instance list, select the instance for which you want to configure a disaster recovery instance, and click **Manage**.
![](//mc.qcloudimg.com/static/img/57f7cf928cf07582c75faa6d672f9dd7/image.png)<br>
Step 2: Make sure the GTID feature has been enabled. Click **Add Disaster Recovery Instance** to enter the disaster recovery instance purchase page.
![](//mc.qcloudimg.com/static/img/293ce146910ff324114bde452dea486b/image.png)<br>
Step 3: On the purchase page, select the region of the disaster recovery instance. After confirming the instance information, click Activate and wait for the delivery of disaster recovery instance.
![](//mc.qcloudimg.com/static/img/b55e7b40b4533d52f63980839f997676/image.png)

### Create a synchronization link
After the delivery of disaster recovery instance, you need to configure a synchronization link for disaster recovery to achieve the remote disaster recovery.

Step 1: In the list of master instances and the "instance details" page, you can view the synchronization status of the disaster recovery instance. If "Unsynchronized" is displayed, click **Create Synchronization** to create a private network synchronization linkage with the master instance for the disaster recovery instance.
![](//mc.qcloudimg.com/static/img/9cf09f7b9f6339b5fafc529fd8953b6d/image.png)
![](//mc.qcloudimg.com/static/img/9ec458d4ce19bee48939df4585058215/image.png)<br>
Step 2: Enter the task name, check the source database and destination database information, and then click **Next**.
![](//mc.qcloudimg.com/static/img/65081661234a42fb80cad12a24e15471/image.png)<br>
Step 3: Select the object to be synced. Synchronization of the entire instance or only part of the database table is supported. Synchronization type cannot be selected for now.
![](//mc.qcloudimg.com/static/img/76c331f779b11094f13b1d2a03d929c7/image.png)<br>
Step 4: Click **Save and Verify**. After the verification succeeds, you can view the task details on the TencentDB **Data Transfer** page.
![](//mc.qcloudimg.com/static/img/2cc2ee83a7cd428684479fbefb3cb79c/image.png)
![](//mc.qcloudimg.com/static/img/fff3ba47eedc8f85c0a61717aaf80756/image.png)<br>


### Manage disaster recovery instances
1. View disaster recovery instances<br>
Disaster recovery instances can be viewed in the region to which they belongs. You can filter out all the disaster recovery instances of a region in the **Instance Type** of the instance list. For each disaster recovery instance, you can view the master instance information using the icon under the instance name.
![](//mc.qcloudimg.com/static/img/5a6b1fde4c29a231fc88cdf0eeb127d7/image.png)
2. View synchronization latency<br>
You can view the synchronization latency between the master instance and the disaster recovery instance at the top of the instance details page.
![](//mc.qcloudimg.com/static/img/d3be4dee430091154466a5164910da64/image.png)
3. Features of disaster recovery instance<br>
Disaster recovery instance provides instance details, instance monitoring, backup management, and slow log features that can be viewed in the console.
![](//mc.qcloudimg.com/static/img/78b5dd4673d6b1edb4409bd906c2a01a/image.png)

### Upgrade a disaster recovery instance to a master instance
You can quickly upgrade a disaster recovery instance to a master instance in the console. After the switching, the synchronization connection between the disaster recovery instance and the master instance is broken, and the instance database data write capability and the full TencentDB features are restored.
Once the synchronization connection is broken, it cannot be reestablished. Please proceed with caution.
![](//mc.qcloudimg.com/static/img/1f2345005497a7d1aedc2f2c725d3c3e/image.png)

### Switch a disaster recovery instance back to a master instance
After the service is resumed in the region where the master instance resides, you can, with the help of TencentDB service personnel, perform reverse data synchronization and data verification, and then switch the disaster recovery instance back to the master instance.

## Notes
1. If the cold backup before rollback or disaster recovery does not contain the table, the rollback or disaster recovery will fail.
2. If the rollback or disaster recovery involves composite operations on other database tables during the trace of binlog, the statement may fail.
3. If the rollback or disaster recovery involves table's foreign key and other constraints during the trace of binlog, SQL statements may fail.

