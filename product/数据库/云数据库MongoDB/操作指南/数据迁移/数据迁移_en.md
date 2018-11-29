## How to Use MongoDB Migration Tool
## 1. Overview of Self-built Instance Migration
Currently, Tencent Cloud MongoDB supports two types of migration: self-built CVM instance migration and public network instance migration.
#### 1.1 Glossary

| Term | Description | 
|---------|---------|
| Source Instance | Source instance of the migration | 
| Destination Instance | Destination instance of the migration, i.e. Tencent Cloud MongoDB instance purchased by the user | 
| Server | The server in which the source instance of the migration resides | 

#### 1.2 Notes on Migration
1.	To ensure migration efficiency, you cannot migrate self-built CVM instance to other regions;
2.	When migrating public network instance, please ensure that the source instance service is accessible under public network environment;
3.	When the migration succeeds, you can disconnect from the source instance and switch the connection to destination instance after the data is verified at business side.
4.	[Important] If the self-built instance is a single node, you cannot perform online migration, as no oplog is supported for a single node.

## 2. Migration Procedure
#### 2.1 Creating a Migration Task
Enter the "Migration Task List" and create a migration task by following the steps below:
1.	Select the region to which the destination instance belongs;
2.	Click "New Instance Migration Task" to go to the "New Migration Task" page;
![](https://mc.qcloudimg.com/static/img/164c0ebdd2ce7a9a171c9be0727b6cb3/1.1.png)

#### 2.2 Entering Basic Information
The following description is based on MongoDB instance on CVM. The same is applicable to the public network instance migration.

| Field | Description | Use | Required | 
|---------|---------|---------|---------|
| Task name | Name of the migration task | Used by users for their management of tasks | Yes |
| CVM ID | ID of the Tencent CVM in which the source MongoDB instance resides | The migration task will check the operation status of the CVM with this ID. For public network instance migration, it can be left empty | Yes |
| MongoDB IP | Private IP of the Tencent CVM in which the source MongoDB instance resides | The migration task will check the private IP of the CVM | Yes |
| Port | Port number of source instance | The migration task will access the source instance service | Yes |
| Password | Source instance password | Used for authentication for accessing the source instance service | Yes |
| Destination database-instance | Destination instance ID | Data is synchronized to the destination instance | Yes |
![](https://mc.qcloudimg.com/static/img/77fb157b0783b3706e5bd7f97d3eb6fb/2.png)

#### 2.3 Selecting the Migration Object
Currently, database-level migration is supported. Check the database to be migrated. Click **Save** to create a task.
![](https://mc.qcloudimg.com/static/img/d04abd9d68433d3377adfe97cdf9ebf3/4.png)


After the task is created, it will be displayed in the task list.
![](https://mc.qcloudimg.com/static/img/346f74a2a400e9ef851d35412cb8dfb4/5.png)

#### 2.4 Starting the Migration Task
When the task is created successfully, it is still in a non-activated status. Click **Start** to start the task. The task will verify parameters.
![](https://mc.qcloudimg.com/static/img/188aace20bea6af2363b6b170409bb4a/6.png)

The migration can only be performed after a successful verification.
![](https://mc.qcloudimg.com/static/img/417733549ad60a3fbcbec475663f762f/7.png)
Special note: If the network is inaccessible, please check the security group of the service to which the source instance belongs. All ports for the security group should be allowed.

#### 2.5 Migration Procedure
Click **Start** in the pop-up box to start the migration.
The migration procedure is divided into 3 steps
1. Data synchronization
2. Index creation
3. "oplog" synchronization
![](https://mc.qcloudimg.com/static/img/4e72afb7a91729bbcc47e9424bc6ff65/8.png)

#### 2.5 Stop Synchronization
When oplog synchronization has reached a specific time, click "Complete" and then click "OK" to complete the data synchronization. This can terminate the synchronization of oplog and flag the task as "completed". (You can verify the data on the destination instance. If the verification is passed, the synchronization can be stopped.)
If you want to stop the migration process, you can click **Abort Task**. This will roll back all the synchronized operations and flag the task as "failed".

![](https://mc.qcloudimg.com/static/img/d4f8a746fb7be7c172088ce808d13fc1/9.png)

![](https://mc.qcloudimg.com/static/img/e56d0392b9e0fc287eec5ee1e8fcfd12/10.png)
