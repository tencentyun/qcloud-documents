# Disaster Recovery Instances

## 1. Introduction
For application with a strong demand for continued services and reliable data or regulatory requirements, TencentDB provides disaster recovery instances to help users enhance their capability to deliver continued services at a low cost and improve data reliability.


## 2. Features
* Provide a separate database connection address. Disaster recovery instances can provide read access capability for connection to the nearest network, data analysis and other scenarios, with low device redundancy cost.
* A highly available master/slave architecture is put in place to protect databases from single point of failure (SPOF) risks.
* Charge on an hourly basis. Immediate activation or deactivation is supported. Tiered prices are available; the longer the service is used, the more the discount is offered.
* **Disaster recovery instance synchronization can be achieved through Direct Connect, with a lower synchronization latency, higher stability, and far better synchronization link quality than public network.**
* During the current promotion period, Direct Connect is free of charge and charges for commercialized use will be announced later.



## 3. How It Works
* In a scenario where a Tencent Cloud database is used as a disaster recovery database, disaster recovery instance is the backup of the master instance database.	
* When the master instance changes, logs that record such change will be copied to the disaster recovery instance, and you can synchronize the data by re-playing the logs.
* If the master instance fails, you can activate the disaster recovery instance in seconds and restore the full read/write functions.

## 4. Preconditions
* To create a disaster recovery instance, the master instance has to be MySQL 5.6 or above with the GTID function being enabled.

## 5. Functional Limits
* The disaster recovery instance does not support: project transfer, rollback, SQL operations, parameter configuration, character set change, account management, port change, data import, rollback log, read-only instance functions.

## 6. Steps
### 6.1 Purchase Disaster Recovery Instance
*Step1. In the instance list, select the instance for which you want to configure disaster recovery instance. Click "Manage".
![](//mc.qcloudimg.com/static/img/57f7cf928cf07582c75faa6d672f9dd7/image.png)
*Step2. Make sure the GTID function is enabled. Click "Add Disaster Recovery Instance" to enter the disaster recovery instance purchase page.
![](//mc.qcloudimg.com/static/img/293ce146910ff324114bde452dea486b/image.png)
*Step3. On the purchase page, select the region for the disaster recovery instance. After confirming the instance information is accurate, click the enable button, and then wait for the delivery.
![](//mc.qcloudimg.com/static/img/b55e7b40b4533d52f63980839f997676/image.png)

### 6.2 Create Sync Link
After the disaster recovery instance is delivered, you need to configure the disaster recovery instance synchronization link to implement remote disaster recovery.

*Step1. In the master instance list and the "Instance Details" page, you can view the synchronization status of the disaster recovery instance. If "Not Synchronized" is displayed, click "Create Synchronization" to create a private synchronization link with the master instance for the disaster recovery instance.
![](//mc.qcloudimg.com/static/img/9cf09f7b9f6339b5fafc529fd8953b6d/image.png)
![](//mc.qcloudimg.com/static/img/9ec458d4ce19bee48939df4585058215/image.png)
*Step2. Fill in the task name, confirm the source database information and the destination database information, and then click "Next".
![](//mc.qcloudimg.com/static/img/65081661234a42fb80cad12a24e15471/image.png)
*Step3. Select the object to be synchronized. Synchronization of the entire instance or only part of the database table is supported. Synchronization types cannot be selected currently.
![](//mc.qcloudimg.com/static/img/76c331f779b11094f13b1d2a03d929c7/image.png)
*Step4. Click "Save and Verify" and you can view task details on the TencentDB "Data Transmission" page after verification is successful.
![](//mc.qcloudimg.com/static/img/2cc2ee83a7cd428684479fbefb3cb79c/image.png)
![](//mc.qcloudimg.com/static/img/fff3ba47eedc8f85c0a61717aaf80756/image.png)


### 6.3 Manage Disaster Recovery Instances
1. View disaster recovery instances

	Disaster recovery instances can be viewed from the region where they reside. You can filter out all the disaster recovery instances via the "Instance Type" in the instance list. For each disaster recovery instance, you can view the master instance information using the icon under the instance name.
![](//mc.qcloudimg.com/static/img/5a6b1fde4c29a231fc88cdf0eeb127d7/image.png)

2. View synchronization latency

	You can view the synchronization latency between the master instance and the disaster recovery instance at the top of the instance details page.
![](//mc.qcloudimg.com/static/img/d3be4dee430091154466a5164910da64/image.png)

3. Disaster recovery instance functions

	Disaster recovery instance provides instance details, instance monitoring, backup management, and slow query log functions that can be viewed on the console.
![](//mc.qcloudimg.com/static/img/78b5dd4673d6b1edb4409bd906c2a01a/image.png)

### 6.4 Disaster Recovery Instance Upgrade to Master Instance
You can upgrade the disaster recovery instance to the master instance on the console by just one click. After switching, the synchronization link with the master instance will be disconnected, and the capability to write instance database data and the full TencentDB function restored.
The disconnected synchronization cannot be reconnected. Please proceed with caution.
![](//mc.qcloudimg.com/static/img/1f2345005497a7d1aedc2f2c725d3c3e/image.png)

### 6.5 Switch Back to Master Instance from Disaster Recovery Instance
After the services are restored in the master instance's region, the TencentDB service personnel can assist users to do reverse data synchronization and data verification, after which the instance switch-back can be realized.

## 7. Special Notes
1. If the cold backup before rollback or disaster recovery does not contain the table, the rollback or disaster recovery will fail.
2. If the rollback or disaster recovery, while tracing binlog, involves composite operations of other database table, the statement may fail.
3. If the rollback or disaster recovery, while tracing binlog, involves foreign key and other restrictions in the table, SQL statements may fail.
