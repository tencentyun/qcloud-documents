###  Memory Use
**Q: Why does the monitor show high memory utilization of mongoDB?**
A: MongoDB uses a greedy strategy to try to allocate available memory for caching to improve performance, especially for the Mmap engine. Users don't need to worry about a higher memory usage

###  Connection
**Q: What is the specification for number of connection? Does it support connection upgrade?**
A: Connection specification reference: [Connection Restrictions](https://cloud.tencent.com/document/product/240/622). The number of connections is related to instance specifications. You can obtain more connections by upgrading instance specifications.

**Q: How to set the maximum number of connections for php?**
A:
•	MongoDB driver ([Official PHP Documentation](http://php.net/manual/en/set.mongodb.php)) can control the number of connections by configuring the maxPoolSize parameter in the URL connection
•	MongoDB ([Official PHP Documentation](http://php.net/manual/en/set.mongodb.php)) driver can set the number of connections through Mongo::setPoolSize() method http://php.net/manual/en/mongopool.setsize.php

**Q: After connecting, it prompts "tencent cloud mongodb platform ****. What does this version number stand for?**
A: This is Tencent Cloud's internal version log, and has nothing to do with MongoDB official version. Users do not need to worry about it.


### Rollback and Backup
**Q: How long will rollback take?**
A: Rollback is based on the latest full backup image + oplog. The rollback time is determined by the amount of oplog playback. If the rollback is performed a long time after the full backup is completed, it will take much time for oplog playback.

**Q: Is backup file download supported?**
A: Not supported for now.

**Q: Why the previous backup files are missing with replacement operation after rollback?**
A: After replacement, the original backup file is no longer applicable to the replaced instance. So the backup file will be deleted in the rollback process.

**Q: Replacement operation is done after rollback. Can I roll back again?**
A: No. After replacement, the original backup file is no longer applicable to the replaced instance, so users are unable to roll back again. Users must confirm it before performing the replacement operation.

**Q: After rollback, what is the difference between a conversion operation and a replacement operation?**
A: Conversion is to convert the rolled-back temporary instance to a formal instance, which has no mapping relationship with the original one. By default, the temporary instance has a validity period of 2 days. Please renew in time.
Replacement is to overwrite the current instance data with the temporary instance data. After replacement, the backup file of the instance will be deleted and the instance cannot be rolled back. Please proceed with caution.


### MongoDB Version
**Q: What is the current version of MongoDB on the cloud?**
A: 3.2.10

**Q: Does it support to switch instances on the cloud from the Mmap engine to the Wt engine?**
A: It is not supported for now. We are developing a migration tool to online synchronize data from one cloud instance to another one. And you can use the tool then.

### Upgrade
**Q: How long does it take to upgrade instance specifications? Will the use of instance be affected by upgrade?**
A: The time required for upgrading instance specifications depends on the used capacity of the instance. A master switching of instance occurs during the upgrade, and the instance will be temporarily inaccessible for about ten seconds.

**Q. How does it upgrade?**
A:
Step 1: Add a node of new specification to the cluster;
Step 2: Wait until the data synchronization of the new node completed;
Step 3: Delete the old node, and the upgrade is completed.

**Q: Is timed upgrade supported?**
A: It is under development and will be supported soon.


### Features
**Q: How to get a slow query of an instance?**
A: Please refer to the official website for slow log details. Slow log analysis and download features will be launched soon.

**Q: Is public network supported?**
A: No. If you need public network, you need to set up proxy directly.

**Q: Is passwordless access supported?**
A: For security reasons, passwordless access is not supported.


**Q: mongodump is unable to export data**
A: mongodump [Import and Export](https://cloud.tencent.com/document/product/240/5321). It is recommended to use mongodump 3.2.10 or later.

**Q: How to set dump from database?**
A: In mongodump parameters, set readPreference=secondaryPreferred


**Q: Does Cloud Database MongoDB support public network access?**
A: Temporarily not, you need to purchase a CVM, and access through private network

**Q: Which regions are on sale?**
A: Guangzhou, Shanghai, Beijing, Hong Kong, Shanghai Finance Zone and Shenzhen Finance Zone. Other regions are under testing, and will gradually become available.

**Q: Does Cloud Database MongoDB support adding Secondary nodes dynamically?**
A: The feature is not supported for the moment as it is under alpha test. It will be available in the future.

**Q: Does Cloud Database MongoDB support sharding?**
A: Supported.

**Q: What is the difference between Cloud Database MongoDB and self-built MongoDB?**
A: Please see [Product Advantages](http://cloud.tencent.com/doc/product/240/%E4%BA%A7%E5%93%81%E4%BC%98%E5%8A%BF)

**Q: Which languages of the clients are supported by Cloud Database MongoDB?**
A: Cloud database MongoDB provides the same compatibility with client connections as MongoDB. Cloud database MongoDB supports any client that is supported by official MongeDB. For example: C, C++, c#, java, node.js, python, php, perl, etc. For more information, see official website at [https://docs.mongodb.org/ecosystem/drivers/](https://docs.mongodb.org/ecosystem/drivers/).

**Q: How to connect to Tencent Cloud MongoDB in shell?**
A: Please see [Shell Connection Example](https://cloud.tencent.com/doc/product/240/3978).

**Q: What does the URIs in service applications look like, that are used to connect to MongoDB?**
A: Please see [Connection Examples](https://cloud.tencent.com/doc/product/240/3563).

**Q: Which version of the driver should I choose?**
A: Use the latest version if you can, for example, use mongo-1.6 or above for PHP

**Q: Why can't I connect to Tencent Cloud MongoDB using meteor and other types of frameworks and class libraries?**
A: This is usually caused by incorrect connection method or URI combinations, please verify these factors first

**Q: Sometimes the connection condition becomes good/bad?**
A: We will terminate idle connections if there are no accesses in a long time. If the driver cannot auto-reconnect, you will need to reconnect via application (reference: retry 3 to 5 times, sleep for around 100ms)

**Q: How big is oplog? Can I adjust it?**
A: oplog occupies 10% of the instance's capacity and does not support size adjustment.

**Q: Is oplog included in the purchased capacity?**
A: Since oplog exists inside the MongoDB database, it will occupy part of the capacity purchased by users (default is 10%)
 
**Q: How often does Tencent Cloud Database MongoDB back up files? How long is the data retained?**
A: Now, all instances will automatically back up every day, while users can also initiate a manual backup. Backup data will be retained for 5 days.

**Q: Can I roll back data to any point of time using Tencent Cloud Database MongoDB's rollback function?**
A: Backup data is retained for 5 days, you can roll back to any time point within 5 days. In particular, it is necessary to select a time point between two backups for rollback operation (if there is no backup behind the time point to which you wish to roll back, you can simply perform a manual backup). In addition, if the data operation between two backups caused total oplog data flow to exceed 10% of instance capacity, you will not be able to roll back data to a time point between these two backups.

**Q: Which permissions are currently available?**
A: For now, only [RoleDBAdminAny and RoleReadWriteAny](https://docs.mongodb.org/v3.0/reference/built-in-roles/) are available; root is temporarily unavailable; more roles will become available in the future. We will also open up more convenient and practical management console features to replace the need to call for some special permissions.

**Q: Why does the data imported into Tencent Cloud MongoDB instance occupy less space compared to self-built MongoDB?**
A: A possible reason is that there are a large number of addition, deletion and modification operations accumulated after the database has been running for a long time. MongoDB will allocate a larger space than the actual data size during write operations in order to improve performance, and the original space is not reused after the data is deleted, resulting in an overall higher void rate in the entire database space. Meanwhile, importing data can be considered as an operation similar to disk defragging, which makes imported data more compact and appears smaller in size.

**Q: According to show dbs or monitoring data, why does the database occupy more space than the actual data size?**
A: The occupied space displayed in show dbs or in the monitoring data includes the oplog data, which occupies 10% capacity of the selected disk by default
Additional space is required to store BSON structure and index when inserting data, thus the storage space will be larger than the actual data size
The MMAPv1 engine currently used will allocate additional space to store a single data entry, which will occupy more space

**Q: How to use mongoose to connect to Tencent Cloud Database MongoDB?**
A: [See BBS](http://bbs.qcloud.com/thread-17852-1-1.html)

**Q: What happens if disk usage reaches 100%?**
A: At this point the instance will banned, in which case it will become read-only, any connections for write attempt will be closed. Please pay attention to your business development and instance usage, expand capacity as appropriate when capacity usage reaches a certain level.

**Q: What should I do if I lose disconnection or encounter the "Remote server has closed the connection" message?**
A: First of all, see [Connection Examples](https://cloud.tencent.com/doc/product/240/3563) to eliminate authentication issues; if you can connect but still encounter this problem, you may need reconnection mechanism. See [Reconnection](https://cloud.tencent.com/doc/product/240/4980).

