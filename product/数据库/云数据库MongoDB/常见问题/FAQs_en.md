#### FAQS

**Q: Does Cloud Database MongoDB support public network access?**
A: Temporarily not, you need to purchase a CVM, and access through private network

**Q: Which regions are on sale?**
A: Guangzhou, Shanghai, Beijing, Hong Kong; other regions are under testing, and will gradually become available

**Q: Does Cloud Database MongoDB support adding Secondary nodes dynamically?**
A: Temporarily not, the feature is under alpha test and will be available in the future

**Q: Does Cloud Database MongoDB support sharding?**
A: Temporarily not, the feature is under alpha test and will be available in the future

**Q: What is the difference between Cloud Database MongoDB and self-built MongoDB?**
A: Please see [Advantage of Cloud Database MongoDB over Self-built MongoDB](http://www.qcloud.com/doc/product/240/%E4%BA%A7%E5%93%81%E4%BC%98%E5%8A%BF)

**Q: Which languages of the clients are supported by Cloud Database MongoDB?**
A: All connections between Cloud Database MongoDB and clients are compatible with MongoDB. The Cloud Database supports any client that is supported by official MongeDB. For example: C, C++, c#, java, node.js, python, php, perl, etc., please see official website at [https://docs.mongodb.org/ecosystem/drivers/](https://docs.mongodb.org/ecosystem/drivers/) for more information

**Q: How to connect to Tencent Cloud MongoDB in shell?**
A: Please see [Shell Connection Example](https://www.qcloud.com/doc/product/240/3978)

**Q: What does the URIs in service applications look like, that are used to connect to MongoDB?**
A: Please see [Connection Examples] (https://www.qcloud.com/doc/product/240/3563)

**Q: Which version of the driver should I choose?**
A: Use the latest version if you can, for example, use mongo-1.6 or above for PHP

**Q: Why can't I connect to Tencent Cloud MongoDB using meteor and other types of frameworks and class libraries?**
A: This is usually caused by incorrect connection method or URI combinations, please verify these factors first

**Q: Sometimes the connection condition becomes good/bad?**
A: We will terminate idle connections if there are no accesses in a long time. If the driver cannot auto-reconnect, you will need to reconnect via application (reference: retry 3 to 5 times, sleep for around 100 ms)

**Q: How big is oplog? Can I adjust it?**
A: oplog occupies 10% of the instance's capacity and does not support size adjustment

**Q: Is oplog included in the purchased capacity?**
A: Since oplog exists inside the MongoDB database, it will occupy part of the capacity purchased by users (default is 10%)
 
**Q: How often does Tencent Cloud Database MongoDB back up files? How long is the data retained?**
A: Currently, all instances will automatically back up every day, while users can also initiate a manual backup. Backup data will be retained for 5 days.

**Q: Can I roll back data to any point of time using Tencent Cloud Database MongoDB's rollback function?**
A: Backup data is retained for 5 days, you can roll back to any time point within 5 days. In particular, it is necessary to select a time point between two backups for rollback operation (if there is no backup behind the time point to which you wish to roll back, you can simply perform a manual backup). In addition, if the data operation between two backups caused total oplog data flow to exceed 10% of instance capacity, you will not be able to roll back data to a time point between these two backups.

**Q: Can I download the backups?**
A: Temporarily not, it is under alpha test and will be available in the future

**Q: Which permissions are currently available?**
A: Currently, only [RoleDBAdminAny and RoleReadWriteAny] (https://docs.mongodb.org/v3.0/reference/built-in-roles/) are available; root is temporarily unavailable; more roles will become available in the future. We will also open up more convenient and practical management console features to replace the need to call for some special permissions.

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
A: First of all, see [Connection Examples](https://www.qcloud.com/doc/product/240/3563) to eliminate authentication issues; if you can connect but still encounter this problem, you may need reconnection mechanism. See [Reconnection](https://www.qcloud.com/doc/product/240/4980)

